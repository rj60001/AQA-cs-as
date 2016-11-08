def choice():
    BCType = input('What barcode type are you using? [upc/isbn-10/isbn-13]')
    while BCType != ('upc' or 'isbn-10' or 'isbn-13'):
        BCType = input('What barcode type are you using? [upc/isbn-10/isbn-13]')
    
    return BCType

def codeEntry():
    Code = input('Please type in your relative code: ')
    return Code

def check(type, code):
    if type == 'upc':
        while len(code) != 12:
            code = print('Invalid please try again: ')+codeEntry()
    elif type == 'isbn-10':
        while len(code) != 10:
            code = print('Invalid please try again: ')+codeEntry()
    elif type == 'isbn-13':
        while len(code) != 13:
            code = print('Invalid please try again: ')+codeEntry()

def init():
    BCType = choice()
    while BCType != ('upc' or 'isbn-10' or 'isbn-13'):
        BCType = choice()
    
    code = codeEntry()
    while Code.isnumeric() == False:
        code = codeEntry()
    
    check(BCType, Code)

