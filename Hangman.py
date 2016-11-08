
import string

alphabet= string.ascii_lowercase
alphabetList = list(alphabet)
guess = []
guessList = []
guessWord="computer"

def displayProgress(l):
    if len(guessList) == 8:
        print('Congratulations! You have won!')
        exit()
    
    if l in alphabetList:
        for w in guessWord:
            if w in guessList:
                print(w, end=" ")
            else:
                print("__", end=" ")

            if l in alphabetList:
                alphabetList.remove(l)
    else:
        print('Letter has already been used.')


win = False
while win == False:
    w=input("Give me a letter: ")

    if w in guessWord:
        guessList.append(w)
    
    displayProgress(w)
