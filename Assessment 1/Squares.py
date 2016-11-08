'''
    This program looks at the square result of a user inputed number.
'''

def oddCheck(squareNum):
    if squareNum%2 == 0:
        return 'even'
    elif squareNum%2 != 0:
        return 'odd'

def upperCheck(squareNum):
    squareNumStr = str(squareNum)
    first = squareNumStr[0:1]
    firstNum = float(first)

    if firstNum < 5:
        return 'lower'
    elif firstNum > 5:
        return 'upper'

def init():
    numList = []
    numStr = input('Please type in your number:')
    num = float(numStr)
    squareNum = num**2
    oddEven = oddCheck(squareNum)
    upperLower = upperCheck(squareNum)
    numList += str(squareNum)
    numList += oddEven
    numList += upperLower 

    print(numList)

init()
