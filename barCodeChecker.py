def choice():
    BCType = input('What barcode type are you using? [upc/isbn-10/isbn-13]')
    while BCType != ('upc' or 'isbn-10' or 'isbn-13'):
        BCType = input('What barcode type are you using? [upc/isbn-10/isbn-13]')
    
    return BCType

def check(type, code):
    if type == 'upc':
        #
    elif type == 'isbn-10':
        #
    elif type="isbn-13":
        #

def init():
    BCType = choice()
    Code = input('Please type in your relative code: ')

    while Code.isnumeric() == False:
        Code = input('Please type in your relative code: ')
    
    check(BCType, Code)

