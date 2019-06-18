#! /usr/bin/env python3

import glob
import os

MAIN_FOLDER_PATH = './'
MAIN_FOLDER_FILES = glob.glob('%s*' % (MAIN_FOLDER_PATH))

def get_subfiles():
    folders = []
    files = []

    for path in MAIN_FOLDER_FILES:
        if path.count('.') != 2:
            folders.append(path)

    for path in folders:
        in_path = glob.glob('%s/*' % path)
        
        for path_file in in_path:
            if path_file.count('.') != 2:
                folders.append(path_file)
            else:
                files.append(path_file)

    return files

if __name__ == '__main__':
    subfiles = get_subfiles()
    
    for f in subfiles:
        print(f)