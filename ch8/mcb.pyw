#mcb.pyw - Saves and load pieces of text to clipboard
#Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       py.exe mcb.pyw list - Loads all keywords to clipboard.

import pyperclip, shelve, sys

mcbShelf = shelve.open('mcb')

