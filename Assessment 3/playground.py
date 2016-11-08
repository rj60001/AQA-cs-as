def skipEncrypt(string, skip):
    cipherText = ''
    for i in range(skip, len(string)*(skip+1), skip+1):
        cipherText += string[i%len(string)]
    return cipherText

def skipDecrypt(string, skip):
    plainText = ''
    j = 0
    while j <= 3:
        for i in range(skip, len(string)*(skip+1), skip+1):
            plainText += string[i%len(string)]
        string = plainText
        j = j + 1
    return plainText

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