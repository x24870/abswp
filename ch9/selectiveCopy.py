# Select specified type of file and copy to folder

import os, shutil

def selectiveCopy(folder):
    filetype = '.txt'
    
    absfolder = os.path.abspath(folder)
    
    # If copy folder not exist, create it
    copyfolder = os.path.join(absfolder, 'copy')
    os.makedirs(copyfolder, exist_ok=True)
    
    for foldername, subfolders, filenames in os.walk(absfolder):     
        # Skip loop the copy folder
        if os.path.basename(foldername) == 'copy':
            continue
        
        for filename in filenames:
            if filetype in filename:
                absfilename = os.path.join(foldername, filename)
                print('Copy %s to %s' % (filename, copyfolder))
                shutil.copy(absfilename, copyfolder)
                
    print('Done')
                
if __name__ == '__main__':
    selectiveCopy('.')