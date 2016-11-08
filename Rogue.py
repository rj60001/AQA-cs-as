import random
import os
os.environ['LINES'] = '40'
os.environ['COLUMNS']= '80'

##HERE IS THE BOARD - YOU CAN EDIT IT TO CHANGE THE LAYOUT OF THE ROOMS, POSITIONS OF MONSTERS AND POSITIONS OF HEALING SHRINES
layout='''___________________________________________________________________________
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXX      XXXXXXXXXXXXX      A        XXXXXXXXXXXXX       ?    X      XXX|
|XXXX   O  XXXXXXXXXXXXX               XXXXXXXXXXXXX  XXXXXXXX  X  B   XXX|
|XXXX                                  XXXXXXXXXX      XXXXXXX         XXX|
|XXXX      XXXXXXXXXXXXX                               XXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXX               XXXXXXXXXX   C  XXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX        XXXXX|
|XXXXXX                 XXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ?    XXXXX|
|XXXXXX  XXXXX  XXXX    XXXXXX  XXXXXXXXXXXXXXXXX      XXXXXX        XXXXX|
|XXXXXX  XXXXX  XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXX  D   XXXXXXXXXXXX  XXXXX|
|XXXXXX  XXXXX                                         XXXX          XXXXX|
|XXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXX     XXXXXXXXXX|
|XXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXX|
|XXXXXX       E       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXX|
|XXXXXXXXXXXXXX   F                                             XXXXXXXXXX|
|XXXXXXXXXXXXXX       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|-------------------------------------------------------------------------|
'''

## THESE GLOBAL VARIABLE DECIDE THE MONSTER AND PLAYER HIT POINTS
playerHP = 20
A = 20
B = 20
C = 20
D = 20
E = 20
F = 20

def genBoard():
    '''This function generates the board - do not change it'''
    board = []
    row = []
    for i in layout:
        row.append(i)
        if i == '\n':
            board.append(row)
            row = []
    return board

def printBoard(board):
    '''This function prints the board - do not change it'''
    for row in board:
        for character in row:
            print(character, end=" ")

def playerTurn(board):
    '''This function decides on players actions - you could potentially add more actions in here'''
    board = move(board,'O')
    return board


def move(board,object):
    oldPos = getObjectPosition(board, 'O')
    newPos = [0, 0]
    b = ''
    squareType = 'z'
    issue = ''

    while squareType != ' ' or squareType == 'A' or squareType == 'B' or squareType == 'C' or squareType == 'D' or squareType == 'E' or squareType == 'F':
        direction = input('What do you want to do?'+issue+' [w/a/s/d]')
        if direction == 'w':
            newPos[0] = oldPos[0] -1
            newPos[1] = oldPos[1]
            squareType = checkSquare(board, newPos)
        elif direction == 'a':
            newPos[0] = oldPos[0]
            newPos[1] = oldPos[1] -1
            squareType = checkSquare(board, newPos)
        elif direction == 's':
            newPos[0] = oldPos[0] +1
            newPos[1] = oldPos[1]
            squareType = checkSquare(board, newPos)
        elif direction == 'd':
            newPos[0] = oldPos[0]
            newPos[1] = oldPos[1] +1
            squareType = checkSquare(board, newPos)
        
        if squareType == ('A' or 'B' or 'C' or 'D' or 'E' or 'F'):
            fight(squareType)
            b = moveMonsters(b)
            printBoard(b)
    
    b = setObjectPosition(board, 'O', newPos, oldPos)
    b = moveMonsters(b)
    printBoard(b)

def moveMonsters(board):
    '''This function moves monsters around the board'''
    monsters = ['A','B','C','D','E','F']
    b = board

    for i in range(0, len(monsters)):
        num = random.randint(0, 3)
        monster = monsters[i]
        oldPos = getObjectPosition(board, str(monster))
        newPos = [0, 0]

        if num == 0:
            newPos[0] = oldPos[0] -1
            newPos[1] = oldPos[1]
            squareType = checkSquare(b, newPos)
            if squareType == ' ':
                b = setObjectPosition(b, str(monster), newPos, oldPos)
            elif squareType == 'O':
                fight(monster)
        elif num == 1:
            newPos[0] = oldPos[0]
            newPos[1] = oldPos[1] -1
            squareType = checkSquare(b, newPos)
            if squareType == ' ':
                b = setObjectPosition(b, str(monster), newPos, oldPos)
            elif squareType == 'O':
                fight(monster)
        elif num == 2:
            newPos[0] = oldPos[0] +1
            newPos[1] = oldPos[1]
            squareType = checkSquare(b, newPos)
            if squareType == ' ':
                b = setObjectPosition(b, str(monster), newPos, oldPos)
            elif squareType == 'O':
                fight(monster)
        elif num == 3:
            newPos[0] = oldPos[0]
            newPos[1] = oldPos[1] +1
            squareType = checkSquare(b, newPos)
            if squareType == ' ':
                b = setObjectPosition(b, str(monster), newPos, oldPos)
            elif squareType == 'O':
                fight(monster)
            
    return b

def getObjectPosition(board,object):
    '''Finds specific objects on the board'''
    for y,row in enumerate(board):
        for x, thing in enumerate(row):
            if thing == object:
                print(thing)
                position = [y,x]
                return position

def setObjectPosition(board,object,newPosition,oldPosition):
    '''sets a new position for an object'''
    board[oldPosition[0]][oldPosition[1]] = ' '
    board[newPosition[0]][newPosition[1]] = object
    return board

def checkSquare(board,newPosition):
    'checks what is in a square'''
    square = board[newPosition[0]][newPosition[1]]
    return(square)

# Finish this function so the hero "O" can fight the monsters.
def fight(monster):
    damage = random.randint(0, 10)
    mDamage = random.randint(0, 6)
    exec(monster+' -= '+str(damage))
    exec('playerHP -= '+str(mDamage))
    print('Monster lost '+str(damage)+' HP. Player lost '+str(mDamage)+' HP.')

def mainLoop():
    '''Runs the game'''
    board1 = genBoard()
    board = board1
    printBoard(board)
    vBool = True
    vTurn = 0 #0 == Player, 1 == Monsters.
    while vBool == True:
        if(vTurn == 0):
            playerTurn(board)
            #vTurn = 1
        elif(vTurn == 1):
            moveMonsters()
            vTurn = 0

mainLoop()
