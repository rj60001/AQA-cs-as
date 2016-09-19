def getName(playerNum):
    name = input('What is Player'+str(playerNum)+'\'s name?')

    while name.isnumeric() == True:
        print('Name cannot be numeric. Please try again.')
        name = input('What is Player'+str(playerNum)+'\'s name?')

    if name.isnumeric() == False:
        return name

def game(playerScore, playerName):
    print(playerName+', your turn!')
    scoreString = input('Please enter a number:')

    while scoreString.isnumeric() == False or int(scoreString) > 10 or int(scoreString) < 1:
        print('score cannot contain non-numeric characters. Please try again')
        scoreString = input('Please enter a number:')
    
    if scoreString.isnumeric() == True:
        scoreCurrent = int(scoreString)
    
    playerScore += scoreCurrent
    return playerScore

def init():
    p1Name = getName(1)
    p2Name = getName(2)

    p1Score = 0
    p2Score = 0

    pTurn = False #False == P1, True == p2

    while p1Score != 100 and p2Score != 100:
        if pTurn == False:
            p1Score = game(p1Score, p1Name)
            if p1Score >= 100:
                print(p1Name+', you won!')
                exit()
            
            pTurn = True
        elif pTurn == True:
            p2Score = game(p2Score, p2Name)
            if p2Score >= 100:
                print(p2Name+', you won!')
                exit()
            
            pTurn = False

init()
