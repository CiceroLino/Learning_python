#THE CHAPTER PROJETCS

#PROJECT: An insecure password locker program.

PASSWORDS = {'email': 'evil_dragon_lord@email.com', 'blog': 'Angry Birds', 'Credit Card': '123456' }

import sys, pyperclip

if len(sys.argv) > 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   #first command line arg is the accout name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[accoun])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

