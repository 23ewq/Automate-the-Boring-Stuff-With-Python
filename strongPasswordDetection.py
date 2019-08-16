# Uses regrex to determine if given password is "strong" - Has at least 8
# characters at least one uppercase letter, one lower case letter, and one number

import re

def isStrong(password):
    if len(password) < 8:
        return False
    passwordRegex = re.compile(r'[a-z]')
    if passwordRegex.search(password) == None:
        return False
    passwordRegex = re.compile(r'[A-Z]')
    if passwordRegex.search(password) == None:
        return False
    passwordRegex = re.compile(r'[0-9]')
    if passwordRegex.search(password) == None:
        return False
    return True

print(isStrong('Random12345'))
