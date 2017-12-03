#bulletPointAdder - add a star sign and space in front on a line

import pyperclip

inputStr = pyperclip.paste()

print('pyperclip input data type: ' + str(type(inputStr)))

splitInput = inputStr.split('\n')

for item in splitInput:
    item = '* ' + item
    print(item)

outputStr = '\n'.join(splitInput)
    
pyperclip.copy(outputStr)