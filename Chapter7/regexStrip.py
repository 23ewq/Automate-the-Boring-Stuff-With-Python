"""Write a function that takes a stringand does the same thingas
the strip() string method.  If no other arguments are passed
other than the string to strip, then whitespace characters will be removed
from the beginning and end of the string. Otherwise, the characters specified
in the second argument to the function will be removed from the string.
"""

import re

def regex_strip(string, remove = ' '):
    strip_regex = re.compile('[{}]'.format(remove))
    print(strip_regex.sub('', string))

regex_strip("Hello I am John", 'z')
