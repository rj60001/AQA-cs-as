print("Player One enter your chosen number: ")
NumberToGuess = int(input())
while NumberToGuess < 1 or NumberToGuess > 10:
    print("Not a valid choice, please enter another nunber: ")
    NumberToGuess = int(input())
Guess = 0
NumberOfGuesses = 0
while Guess != NumberToGuess and NumberOfGuesses < 5:
    print("Player Two Have a guess: ")
    Guess = int(input())
    NumberOfGuesses += 1

if Guess == NumberToGuess:
    print("Player Two wins")
else:
    print("Player One wins")
