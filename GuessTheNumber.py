'''
    A simple number guessing game!
'''

def init():
    print('This is a game called \'Guess The Number!\' Two players are required: Player One and Player Two.')
    num = input('Player One: you\'re up! Please enter an integer between and inclusive of integer values 1 and 10: ')
    num = int(num)

    while num < 1 or num > 10:
        num =  input('That is an invalid value! Please try again! (Please enter an integer between and inclusive of integer values 1 and 10:) ')
        num = int(num)
    
    guessNum = input('Player Two: your turn! Please enter a guess integer between and inclusive of integer values 1 and 10: ')
    guessNum = int(guessNum)
    guesses = 4

    while guessNum != num:
        if guessNum < 1 or num > 10:
            guessNum =  input('That is an invalid value! Please try again! (Please enter a guess integer between and inclusive of integer values 1 and 10:) ')
            guessNum = int(guessNum)
        elif guesses == 0:
            break
        else:
            guessNum =  input('Incorrect. '+str(guesses)+' attempts remaining! Please try again: ')
            guessNum = int(guessNum)
            guesses -= 1
    
    if guesses == 0 and guessNum != num:
        print('Player One wins!')
    elif guessNum == num:
        print('Player Two wins!')

init()
