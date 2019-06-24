import glob
import os
import re

WITH_ACCENT = ['ü', 'é', 'á', 'í', 'ó', 'ú', 'ñ', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ü']
WITHOUT_ACCENT = ['u', 'e', 'a', 'i', 'o', 'u', 'n', 'A', 'E', 'I', 'O', 'U', 'U']

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
            if not re.match('^[a-zA-Z0-9_]*$', path_file):
                now_path_file = path_file

                for char in '!@#$%^&*()[]{};:,<>?|`~-=_+ ':
                    path_file = path_file.replace(char, '_')

                os.rename(now_path_file, path_file)
            
            new_path_file = None

            for i, char in enumerate(WITH_ACCENT):
                if char in path_file:
                    new_path_file = path_file.replace(char, WITHOUT_ACCENT[i])
            
            if new_path_file:
                os.rename(path_file, new_path_file)
                path_file = new_path_file

            if path_file.count('.') != 2:
                folders.append(path_file)
            else:
                files.append(path_file)

    return files

if __name__ == '__main__':
    subfiles = get_subfiles()
    
    for f in subfiles:
        print(f)