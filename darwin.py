""" mac installer

Install fontman on Mac platforms
"""

import os, shutil, stat, time, wget
from os.path import expanduser

from Operation import Operation
from artifacts import base_url, fms_darwin_64, fms_darwin_86, gui_darwin_64, \
    gui_darwin_86, version
from install import arch, print_info


def install():
    o = Operation()
    time.sleep(1)
    print_info()

    # create fontman home directory
    print("creating fontman directory... :-)")
    home_dir = expanduser('~/')
    fontman_dir = home_dir + 'applications/fontman'
    o.make_directory(fontman_dir)

    # determine system architecture and download artifacts and extract
    print("make sure you have connected to the internet... :-)")

    if '64bit' in arch:
        print("downloading fontman artifacts for darwin x86_64")
        o.download_file(base_url + fms_darwin_64)
        o.download_file(base_url + gui_darwin_64)

        print("extracting...")
        o.extract_archive(fms_darwin_64, fontman_dir)
        o.extract_archive(gui_darwin_64, fontman_dir)

    else:
        print("downloading fontman artifacts for darwin x86")
        o.download_file(base_url + fms_darwin_86)
        o.download_file(base_url + gui_darwin_86)

        print("extracting...")
        o.extract_archive(fms_darwin_86, fontman_dir)
        o.extract_archive(gui_darwin_86, fontman_dir)

    # change mode of artifacts to execute mode
    o.execute_mode(fontman_dir + "/fms")

    # initializing fontman data
    print("initializing fontman data...")
    os.system("cd " + fontman_dir + " && ./fms init")

    print("starting fontman :-)")
    os.system(
        "nohup "+ fontman_dir + "/fms start &> " + fontman_dir+ "/fms.log &"
    )
    os.system(fontman_dir + "/fontman-gui")

    print("\n\nall done ^_^\n you can now close this window.")


if __name__ == '__main__':
    install()
