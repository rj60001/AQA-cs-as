def init():
    mylist = [1, 2, 3, 4, 5]
    outerPointer = 2

    for i in range(outerPointer, len(mylist)):
        currentValue = mylist[outerPointer]
        innerPointer = outerPointer -1
        while innerPointer > 0:
            mylist[innerPointer] = mylist[innerPointer - 1]
            innerPointer = innerPointer - 1

        mylist[innerPointer + 1] = currentValue

    for i in range(0, len(mylist)):
        print(mylist[i], end=' ')

init()
