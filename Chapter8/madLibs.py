# madLibs.py - a Mad Libs program that reads in text files and lets
# the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or
# VERB appears in the text file

textFile = open('textFile.txt', 'r')
string = textFile.read()

grammars = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
for i in grammars:
    print('Enter an ' + i.lower() + ':' )
    x = str(input())
    string = string.replace(i, x)
print(string)
textFile.close()

