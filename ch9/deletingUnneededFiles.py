# Search current folder and subfolders, delete the files those size more than
# 100 MB.

import os

def delNneedFiles(folder):
    absfolder = os.path.abspath(folder)
    
    for foldername, subfolders, filenames in os.walk(absfolder):
        for filename in filenames:
            abspath = os.path.join(foldername, filename)
            size = os.path.getsize(abspath)
            if size > 102400000:
                print('***' + abspath + ' will be delete.')
                os.unlink(abspath)


if __name__ == '__main__':
    delNneedFiles('.')
