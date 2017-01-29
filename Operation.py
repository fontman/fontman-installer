""" Operations

Common operations used by installer scripts
"""

import os
import shutil
import stat
import wget


class Operation:

    def copy_file(self, source, destination):
        print("Copying " + source)
        shutil.copy(source, destination)

    def download_file(self, url, out_dir="."):
        print("downloading " + url)
        wget.download(url, out=out_dir)

    def execute_mode(self, file):
        print("changing mode of " + file + " to group-execute ")
        os.chmod(file, stat.S_IXGRP)

    def extract_archive(self, file_name, dest, type='gztar'):
        print("extracting " + file_name + " to " + dest)
        shutil.unpack_archive(file_name, dest, type)

    def make_directory(self, path):
        print("create directory at " + path)
        try:
            os.makedirs(path)
        except:
            print("Directory already exists or Invalid path.")
