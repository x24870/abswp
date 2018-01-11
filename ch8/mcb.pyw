#mcb.pyw - Saves and load pieces of text to clipboard
#Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       py.exe mcb.pyw list - Loads all keywords to clipboard.

import pyperclip, shelve, sys

shelFile = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    shelFile[sys.argv[2]] = pyperclip.paste()
elif sys.argv[1].lower() == 'list':
    print(list(shelFile.keys()))
    pyperclip.copy(str(list(shelFile.keys())));
elif sys.argv[1] in shelFile:
    print(shelFile[sys.argv[1]])
    pyperclip.copy(str(shelFile[sys.argv[1]]))
else:
    print("Can't find matched key.")

shelFile.close()

