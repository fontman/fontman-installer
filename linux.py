""" linux installer

Install fontman on Linux platforms
"""

import os, shutil, stat, time, wget
from os.path import expanduser

from artifacts import base_url, fms_linux_64, fms_linux_86, gui_linux_64, \
    gui_linux_86, version
from install import arch, print_info


def download_file(url):
    print("downloading " + url)
    wget.download(url)


def execute_mode(file):
    print("changing mode of " + file + " to group-execute ")
    os.chmod(file, stat.S_IXGRP)


def extract_archive(file_name, dest, type='gztar'):
    print("extracting " + file_name + " to " + dest)
    shutil.unpack_archive(file_name, dest, type)


def make_directory(path):
    print("create directory at " + path)
    os.makedirs(path)


def install():
    time.sleep(1)
    print_info()

    # create fontman home directory
    print("creating fontman directory... :-)")
    home_dir = expanduser('~/')
    fontman_dir = home_dir + '.config/fontman'
    make_directory(fontman_dir)

    # determine system architecture and download artifacts and extract
    print("make sure you have connected to the internet... :-)")

    if '64bit' in arch:
        print("downloading fontman artifacts for Linux x86_64")
        download_file(base_url + fms_linux_64)
        download_file(base_url + gui_linux_64)

        print("extracting...")
        extract_archive(fms_linux_64, fontman_dir)
        extract_archive(gui_linux_64, fontman_dir)

    else:
        print("downloading fontman artifacts for Linux x86")
        download_file(base_url + fms_linux_86)
        download_file(base_url + gui_linux_86)

        print("extracting...")
        extract_archive(fms_linux_86, fontman_dir)
        extract_archive(gui_linux_86, fontman_dir)

    # change mode of artifacts to execute mode
    execute_mode(fontman_dir + "/fms")
    execute_mode(fontman_dir + "/fontman-gui")

    # initializing fontman data
    print("initializing fontman data...")
    os.system("cd " + fontman_dir + " && ./fms init")

    # adding fms bash profile
    print("writing fms startup entry")
    with open(home_dir + ".profile", "a+") as profile:
        profile.write("")
        profile.write("# run fontman fms")
        profile.write(
            "nohup "+ fontman_dir + "/fms start &> " + fontman_dir+ "/fms.log &"
        )

    # add application shortcut
    with open(
        home_dir + "/.local/share/applications/fontman.desktop","w+"
    ) as shortcut:
        shortcut.write("[Desktop Entry]\n")
        shortcut.write("Encoding=UTF-8\n")
        shortcut.write("Version=" + version + "\n")
        shortcut.write("Exec=" + fontman_dir + "/fontman-gui\n")
        shortcut.write("Terminal=False\n")
        shortcut.write("Type=Application\n")
        shortcut.write("Comment[en_US]=Most elegant font manager\n")

    print("starting fontman :-)")
    os.system(
        "nohup "+ fontman_dir + "/fms start &> " + fontman_dir+ "/fms.log &"
    )
    os.system(fontman_dir + "/fontman-gui")


    print("\n\nall done :-)")


if __name__ == '__main__':
    install()
