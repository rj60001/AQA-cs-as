'''
This is another form of skip cipher.
The plaintext is re-written by skipping a fixed number of symbols.
The process terminates when all symbols have been re-written in the
new order once. Therefore, the entire ciphertext is exactly
the same length as the plaintext.
'''

# You need to implement the two functions that will encrypt and decrypt.
# Your functions should work for any number of skips chosen.
symbols = [' ', '.', ',', '!', '"', "'", '&', '^', '£', '$', '%', '(', ')', '-', '+', '_', '=']
def strip(s):
    sList = list(s)
    for i in range(0, len(sList)):
        for j in symbols:
            if sList[i] == j:
                sList[i] = ''
    
    result = ''.join(sList)
    return result

def skipEncrypt(s, n):
    sStrip = s
    sList = list(sStrip)
    newText = list(sStrip)
    length = len(sList)-1
    for i in range(0, length, n):
        newPosition = i+n
        if newPosition >= length:
            overflow = newPosition-length
            newText[overflow] = sList[i]
        else:
            newText[newPosition] = sList[i]
    
    result = ''.join(newText)
    return result

'''def skipDecrypt(s, n):
    result = skipEncrypt(s, -n)
    return result'''

def skipDecrypt(s, n):
    sStrip = s
    sList = list(sStrip)
    newText = list(sStrip)
    length = len(sList)
    for i in range(0, length, n):
        newPosition = i-n
        if newPosition <= 0:
            overflow = newPosition+length
            newText[i] = sList[newPosition]
            sList[i] = ' '
        else:
            newText[i] = sList[newPosition]
            sList[i] = ' ' 
    result = ''.join(newText)
    return result

def init():
    choice = input("Hey! Welcome to Encrypt inc. Please type one of the relative commands: 'encrypt' - Encrypt a string. 'decrypt' - Decrypt a string.")
    while True:
        if choice == 'encrypt':
            string = input('What is the string to be encrypted?')
            skipNum = int(input('How many skips do you wish to perform?'))
            result = skipEncrypt(string, skipNum)
            print(result)
        elif choice == 'decrypt':
            string = input('What is the string to be decrypted?')
            skipNum = int(input('How many skips do you wish to perform?'))
            result = skipDecrypt(string, skipNum)
            print(result)
        choice = input("Please type one of the relative commands: 'encrypt' - Encrypt a string. 'decrypt' - Decrypt a string.")

init()
