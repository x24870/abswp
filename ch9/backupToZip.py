# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os, zipfile

def backupToZip(folder):
    absfolder = os.path.abspath(folder)
    print('The folder to be zip: %s \n' % absfolder)

    # Name the zip file
    number = 1
    while True:
        zipName = os.path.basename(absfolder) + '_' + str(number) + '.zip'
        if os.path.exists(zipName):
            number += 1
        else:
            break
        
    # Create zip file
    backupZip = zipfile.ZipFile(zipName, 'w')
    
    # Walk through the folder
    for foldername, subfolders, filenames in os.walk(absfolder):
        backupZip.write(foldername)
        
        for filename in filenames:
            # Don't add zip file
            newBase = os.path.basename(absfolder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            filenameInZip = os.path.join(foldername, filename)
            backupZip.write(filenameInZip)
            print('Add file: ', filenameInZip)

    backupZip.close()
    print('Done')

if __name__ == '__main__':
    backupToZip('.')
