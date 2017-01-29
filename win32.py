""" windows installer

Install fontman on Windows platforms
"""

import os, time, winshell
from os.path import expanduser
from win32com.client import Dispatch

from Operation import Operation
from artifacts import base_url, fms_win_32, fms_win_86, gui_win_32,\
    gui_win_86, version
from install import arch, print_info


def install():
    o = Operation()
    time.sleep(1)
    print_info()

    # create fontman home directory
    print("creating fontman directory... :-)")
    home_dir = expanduser('~/AppData\\Local')
    fontman_dir = home_dir + '\\Fontman'
    temp_dir = fontman_dir + '\\temp'

    o.make_directory(fontman_dir)
    o.make_directory(temp_dir)

    # determine system architecture and download artifacts and extract
    print("make sure you have connected to the internet... :-)")

    if '64bit' in arch:
        print("downloading fontman artifacts for Windows x86_64")
        o.download_file(base_url + fms_win_32, temp_dir)
        o.download_file(base_url + gui_win_32, temp_dir)

        print("extracting...")
        o.extract_archive(temp_dir + "\\" + fms_win_32, fontman_dir)
        o.extract_archive(temp_dir + "\\" + gui_win_32, fontman_dir)

    else:
        print("downloading fontman artifacts for Windows x86")
        o.download_file(base_url + fms_win_86, temp_dir)
        o.download_file(base_url + gui_win_86, temp_dir)

        print("extracting...")
        o.extract_archive(temp_dir + "\\" + fms_win_86, fontman_dir)
        o.extract_archive(temp_dir + "\\" + gui_win_86, fontman_dir)

    # copy fontman assets
    o.copy_file("assets/fontman.ico", fontman_dir)
    o.copy_file("assets/run.bat", fontman_dir)

    # initializing fontman data
    print("initializing fontman data...")
    os.system("cd " + fontman_dir + " && fms.exe init")

    # creating shortcut
    desktop = winshell.desktop()
    path = os.path.join(desktop, "Fontman.lnk")
    target = fontman_dir + "\\run.bat"
    wDir = fontman_dir
    icon = fontman_dir + "\\fontman.ico"

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()

    print("\n\nall done ^_^\n you can now close this window.")

if __name__ == '__main__':
    install()
