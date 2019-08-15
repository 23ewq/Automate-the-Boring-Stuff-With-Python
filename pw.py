#! /usr/local/bin/python3
# pw.py - An insecure password locker program.
PASSWORDS = {'email': '7123601',
             'computer': '123456'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage for Mac: ./pw.py account     - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
