def init():
    num = input('Please enter an integer: ')
    num = int(num)
    
    for i in range(1, num+1):
        result = i*num
        print(str(i)+' x '+str(num)+' = '+str(result))

init()