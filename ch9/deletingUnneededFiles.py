# Search current folder and subfolders, delete the files those size more than
# 100 MB.

import os, shutil

def delNneedFiles(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        print(foldername)
        print(subfolders)
        print(filenames)
        for filename in filenames:
            info = filename




if __name__ == '__main__':
    delNneedFiles('.')
