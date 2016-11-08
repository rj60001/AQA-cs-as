testArray = [45, 6, 89, 12, 2, 34, 17, 23]
LastPass = len(testArray)

while (LastPass !=0) or (SwapMade != False):
    SwapMade = False

    for i in range(0, len(testArray)-1):
        if testArray[i] > testArray[i+1]:
            Temp = testArray[i]
            testArray[i] = testArray[i+1]
            testArray[i+1] = Temp
            SwapMade = True
    
    LastPass = LastPass-1

print(testArray)