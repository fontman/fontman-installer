""" windows installer

Install fontman on Windows platforms
"""

import os, shutil, stat, time, wget
from os.path import expanduser

from artifacts import base_url, fms_win_32, fms_win_86, gui_win_32,\
    gui_win_86, version
from install import arch, print_info


def download_file(url, out_dir):
    print("downloading " + url)
    wget.download(url, out=out_dir)


def execute_mode(file):
    print("changing mode of " + file + " to group-execute ")
    os.chmod(file, stat.S_IXGRP)


def extract_archive(file_name, dest, type='zip'):
    print("extracting " + file_name + " to " + dest)
    shutil.unpack_archive(file_name, dest, type)


def make_directory(path):
    print("create directory at " + path)
    try:
        os.makedirs(path)
    except:
        return


def install():
    time.sleep(1)
    print_info()

    # create fontman home directory
    print("creating fontman directory... :-)")
    home_dir = expanduser('~/AppData\\Local')
    fontman_dir = home_dir + '\\Fontman'
    temp_dir = fontman_dir + '\\temp'

    make_directory(fontman_dir)
    make_directory(temp_dir)

    # determine system architecture and download artifacts and extract
    print("make sure you have connected to the internet... :-)")

#    if '64bit' in arch:
#        print("downloading fontman artifacts for Windows x86_64")
#        download_file(base_url + fms_win_32, temp_dir)
#        download_file(base_url + gui_win_32, temp_dir)

#        print("extracting...")
#        extract_archive(temp_dir + "\\" + fms_win_32, fontman_dir)
#        extract_archive(temp_dir + "\\" + gui_win_32, fontman_dir)

#    else:
#        print("downloading fontman artifacts for Windows x86")
#        download_file(base_url + fms_win_86, temp_dir)
#        download_file(base_url + gui_win_86, temp_dir)

#        print("extracting...")
#        extract_archive(temp_dir + "\\" + fms_win_86, fontman_dir)
#        extract_archive(temp_dir + "\\" + gui_win_86, fontman_dir)

    # initializing fontman data
#    print("initializing fontman data...")
#    os.system("cd " + fontman_dir + " && fms.exe init")

    # add FMS auto start at windows login
    with open("C:\\fms.bat", "w+") as shortcut:
        shortcut.write("[Desktop Entry]\n")
        shortcut.write("Encoding=UTF-8\n")
        shortcut.write("Version=" + version + "\n")
        shortcut.write("Exec=" + fontman_dir + "/fontman-gui\n")
        shortcut.write("Terminal=False\n")
        shortcut.write("Type=Application\n")
        shortcut.write("Comment[en_US]=Most elegant font manager\n")

    print("\n\nall done ^_^\n you can now close this window.")


if __name__ == '__main__':
    install()