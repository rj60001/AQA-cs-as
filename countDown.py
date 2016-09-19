'''
    This is a program that takes a user input and from that, counts down to 0.
'''

vBool = True

def init():
    num = input('Please enter a num number.')

    if(int(num) <= 0):
        print('Alpha input occured. Terminating program.')
        exit()

    if num.isalpha() == True or int(num) <= -999:
        print('Alpha input occured. Terminating program.')
        exit()
    
    for i in range(int(num), -1, -1):
        print(i)

while vBool == True:
    init();
