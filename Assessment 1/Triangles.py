'''
    This program calculates the difference in area between two triangles.
'''
def area(array):
    base = float(array[0])
    height = float(array[1])
    area = base/2 * height
    return area

def difference(area1, area2):
    result = area1 - area2

    if result < 0:
        addresult = result*2
        result += addresult
        return result 
    elif result > 0:
        return result

def init():
    tri1 = []
    tri2 = []
    print('Welcome! This program calculates the difference between two triangles! Please snure all measurements are of the same type (e.g. cm)!')
    tri1 += input('A triangle\'s base length please: ')
    tri1 += input('The same triangle 1\'s height length please: ')
    tri2 += input('Another triangle\'s base length please: ')
    tri2 += input('The same triangle\'s height length please: ')
    tri1area = area(tri1)
    tri2area = area(tri2)
    finalresult = difference(tri1area, tri2area)
    print('The difference is: '+str(finalresult))

init()
