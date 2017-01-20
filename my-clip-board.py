#!/usr/bin/env python
# my-clip-board.py - Saves and loads pieces of text to the clipboard, experimenting with sys.argv and pyperclip
# Usage:    python <filename> save <keyword> - Saves current clipboard to assigned keyword
#           python <filename> <keyword> - Loads keyword to clipboard
#           python <filename> list - Loads all keywords to clipboard


import shelve, sys, pyperclip

def showUsage():
    print('Usage:\n\
        python %s save <keyword> - Saves current clipboard\n\
        python %s <keyword> - Loads keyword to clipboard\n\
        python %s remove <keyword> - Removes keyword from storage\n\
        python %s list - Loads all keywords to clipboard'
        % (sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0]))

def main():
    mcbShelf = shelve.open('my-clip-board')

    # Save or remove clipboard content
    if len(sys.argv) == 3:
        if sys.argv[1].lower() == 'save':
            mcbShelf[sys.argv[2]] = pyperclip.paste()
            print('Your clipboard:\n"' + mcbShelf[sys.argv[2]] + '" \nhas been saved under key "' + sys.argv[2] + '"')
        elif sys.argv[1].lower() == 'remove' and sys.argv[2] in mcbShelf:
            del(mcbShelf[sys.argv[2]])
        else:
            showUsage() 
    # List keywords and load content
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            print('\n'.join(mcbShelf.keys()))
        elif sys.argv[1] in mcbShelf:
            print('Your saved text:\n"' + mcbShelf[sys.argv[1]] + '"\nhas been copied to clipboard')
            pyperclip.copy(mcbShelf[sys.argv[1]])
        else:
            showUsage()
    else:
        showUsage()

    mcbShelf.close()

main()