#Let user input specified text, then search all .txt find in the folder.
#If there is any matched text, print it out the file name and line number.

import re, os

stext = input('Enter the text that you want to search. ')

stextReg = re.compile(stext)

fileList = os.listdir()

for filename in fileList:
    if '.txt' in filename:
        with open('%s' % filename) as file:
            text = file.read()
            if stextReg.search(text) != None:
                print('Found matched text in : %s' % filename)

