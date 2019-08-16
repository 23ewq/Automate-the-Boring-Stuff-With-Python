""" tablePrinter.py takes a list of lists (all of the inner lists need to
have the same length) and displays it in a well-organized table with
each column right-justified. Variable tableData holds a sample list  """

def printTable(lis):
    str = ''
    x = 0
    while x < len(lis[0]):
        for i in range(len(lis)):
            str = str + lis[i][x].rjust(maxItem(lis[i])) + ' '
        str = str + '\n'
        x += 1
    print(str)


def maxItem(lis2):
    return len(max(lis2, key=len))

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
