'''
One form of skip cipher is to hide the real message inside a plaintext.
To decipher, you need to skip a fixed number of letters
 (not include whitespaces, punctuations, quotations marks, brackets etc).
 Repeat the skip pattern and you will get the hidden message.
'''

## The following string has a hidden message inside.
## You don't know how many number of skip is used.
## you need to implement a decipher function to discover the message.

mystr='''I was just thinking how everything looks funny painted on. I'm lying here enjoying it.'''
                       
# This is the decipher function that accepts two parameters.
# S: the plaintext where the message is hidden within
# n: the number of skip

def decipher(s,n):
    s = stripNonLetters(s)
    oldText = list(s)
    newText = []
    res = len(oldText)
    for i in range((n-1), res, n):
        newText.append(oldText[i])
    s = ''.join(newText)
    return s


# this is a function that will
# strip whitespaces, punctuations, quotations marks from the plaintext

def stripNonLetters(s):
    for j in s:
        if j == ' ' or j == '.' or j == "'":
            s = s.replace(j, '')
    return s

num = int(input('Skip number:'))
mystr = decipher(mystr, num)
print(mystr)
             