
number = input("Give me a whole number below 12 ")

valid = False

while valid != True:
    try:
        number = int(number)
        valid = True
    except:
        number = input("Give me a whole number below 12 ")
        
number2 = number
    
while number2 <= number:
    print(str(number) + "x" + str(number2) + "=" + str(number * number2))
    number2 -= 1

    if number2 < 0:
        break

  
