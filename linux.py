""" linux installer

Install fontman on Linux platforms
"""

import os, time
from os.path import expanduser

from artifacts import base_url, fms_linux_64, fms_linux_86, gui_linux_64, \
    gui_linux_86, version
from install import arch, print_info
from Operation import Operation


def install():
    o = Operation()
    time.sleep(1)
    print_info()

    # create fontman home directory
    print("creating fontman directory... :-)")
    home_dir = expanduser('~/')
    fontman_dir = home_dir + '.fontman'
    o.make_directory(fontman_dir)

    # determine system architecture and download artifacts and extract
    print("make sure you have connected to the internet... :-)")

    if '64bit' in arch:
        print("downloading fontman artifacts for Linux x86_64")
        o.download_file(base_url + fms_linux_64)
        o.download_file(base_url + gui_linux_64)

        print("extracting...")
        o.extract_archive(fms_linux_64, fontman_dir)
        o.extract_archive(gui_linux_64, fontman_dir)

    else:
        print("downloading fontman artifacts for Linux x86")
        o.download_file(base_url + fms_linux_86)
        o.download_file(base_url + gui_linux_86)

        print("extracting...")
        o.extract_archive(fms_linux_86, fontman_dir)
        o.extract_archive(gui_linux_86, fontman_dir)

    # copy fontman assets
    o.copy_file("assets/fontman.ico", fontman_dir)

    # change mode of artifacts to execute mode
    o.execute_mode(fontman_dir + "/fms")
    o.execute_mode(fontman_dir + "/fontman-gui")

    # initializing fontman data
    print("initializing fontman data...")
    os.system("cd " + fontman_dir + " && ./fms init")

    # adding fms bash profile
    print("writing fms startup entry")
    with open(home_dir + ".profile", "a+") as profile:
        profile.write("")
        profile.write("# run fontman fms")
        profile.write(
            "nohup "+ fontman_dir + "/fms run &> " + fontman_dir+ "/fms.log &"
        )

    # add application shortcut
    with open(
        home_dir + "/.local/share/applications/fontman.desktop","w+"
    ) as shortcut:
        shortcut.write("[Desktop Entry]\n")
        shortcut.write("Encoding=UTF-8\n")
        shortcut.write("Version=" + version + "\n")
        shortcut.write("Icon=" + fontman_dir + "/fontman.ico\n")
        shortcut.write("Exec=" + fontman_dir + "/fontman-gui\n")
        shortcut.write("Terminal=False\n")
        shortcut.write("Type=Application\n")
        shortcut.write("Comment[en_US]=Most elegant font manager\n")

    print("starting fontman :-)")
    os.system(
        "nohup "+ fontman_dir + "/fms start &> " + fontman_dir+ "/fms.log &"
    )
    os.system(fontman_dir + "/fontman-gui")

    print("\n\nall done ^_^\n you can now close this window.")


if __name__ == '__main__':
    install()
