def check(cashAmount):
    coins = [50, 20, 10, 2, 1]
    result = cashAmount
    
    for i in range(0, len(coins)):
        count = 0
        while result >= 0:
            result -= coins[i]
            count += 1
            if result < 0:
                result += coins[i]
                count -= 1
                break
        
        print(str(coins[i])+' : '+str(count))
        

def init():
    cash = input('How much cash do you need? ')
    cash = int(cash)

    result = check(cash)

init()