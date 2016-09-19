'''
    This program checks for an even number.
'''

def init():
    num = input('Type a number.')
    
    if (int(num) % 2) == 0:
         print('This is an even number.')
    elif (int(num) % 2) != 0:
         print('This is an odd number.')
    elif num.isalpha() == true:
        print('This is not a number.')

init()
