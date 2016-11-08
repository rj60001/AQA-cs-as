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
    string = 'hello'
    skipNum = 2
    result1 = skipEncrypt(string, skipNum)
    print('Encrypted: '+result1)
    result2 = skipDecrypt(result1, skipNum)
    print('Decrypted: '+result2)

init()
