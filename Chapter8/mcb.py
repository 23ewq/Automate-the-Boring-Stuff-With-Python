#! /usr/local/bin/python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: ./mcb.py save <keyword> - Saves clipboard to keyword.
#        ./mcb.py.py <keyword> - Loads keyword to clipboard.
#        ./mcb.py list - Loads all keywords to clipboard.
#        ./mcb.py delete <keyword> - Deletes keyword from database
#        ./mcb.py delete - Deletes everything

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'delete':
        for i in mcbShelf.keys():
            del mcbShelf[i]
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
