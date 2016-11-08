'''
    This program takes a postcode and returns it's approximate location.
'''

def init():
    postcode = input('Please enter a postcode: ')
    postcode = postcode.upper()

    if len(postcode) < 5 or len(postcode) > 10:
        print("invalid postcode")
    elif postcode == 'PE10 9JE':
        print("Bourne Grammar School")
    elif postcode[0:3] == 'PE10':
        print("Bourne")
    elif postcode[0:3] == 'PE11':
        print("Stamford")
    elif postcode[0:2] == 'PE':
        print("Somewhere near Peterborough")
    elif postcode[0:2] == 'GU':
        print("That's in Surrey don't you know")
    else:
        print("not too sure")

init()
