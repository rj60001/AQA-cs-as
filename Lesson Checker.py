'''
    This is a program to determine what lesson I have based on my current (as of this time of writing) timetable.
'''

def week():
    w = input('What week is it this week? [1/2]');

    if w != '1' and w != '2':
        print('An error has occured, please type init() to re-initiate.')
        quit()

    return str(w)

def day():
    d = input('What day is it today? [mon/tue/wed/thu/fri]')

    if d == 'mon':
        dInt = 1
    elif d == 'tue':
        dInt = 2
    elif d == 'wed':
        dInt = 3
    elif d == 'thu':
        dInt = 4
    elif d == 'fri':
        dInt = 5
    elif d != 'mon' and d != 'tue' and d != 'wed' and d != 'thu' and d != 'fri':
        print('An error has occured. Please type \'init()\' to reinitiate the program.')
        quit()

    return dInt;

def period():
    p = input('What period is it at the moment? [1/2/3/4/5]')

    if p != '1' and p != '2' and p != '3' and p != '4' and p != '5':
        print('An error has occured. Please type \'init()\' to reinitiate the program.')
        quit()

    return str(p)

def init():
    w1D1 = ['Mathematics - Statistics', 'Biology - RS', 'Computing', 'Study', 'Economics']
    w1D2 = ['Lecture', 'Biology - TV', 'Non-Contact Period', 'Mathematics - Core', 'Computing']
    w1D3 = ['Economics', 'Economics', 'Computing', 'Enrichment Programme', 'Enrichment Programme']
    w1D4 = ['Mathematics - Statistics', 'Mathematics - Core', 'Economics', 'Study', 'Biology - RS']
    w1D5 = ['Mathematics - Core', 'Economics', 'Non-Contact Period', 'Biology - TV', 'Computing']
    w2D1 = ['Economics', 'Biology - RS', 'Study', 'Computing', 'Mathematics - Core']
    w2D2 = ['Lecture', 'Non-Contact Period', 'Mathematics - Core', 'Biology - TV', 'Biology - TV']
    w2D3 = ['Study', 'Non-Contact Period', 'Computing', 'Economics', 'Enrichment Programme']
    w2D4 = ['Computing', 'Computing', 'Biology - RS', 'Non-Contact Period', 'Mathematics - Statistics']
    w2D5 = ['Mathematics - Core', 'Mathematics - Core', 'Economics' 'Biology - TV', 'Computing']

    w = week()
    d = day()
    p = period()

    pIndex = int(p)-1
    x = 'w'+w+'D'+str(d)
    exec('rlist = '+x)
    exec('lesson = rlist[pIndex]')
    exec('print("This lesson would be: "+lesson+". Please type \'init()\' to reinitiate the program.")')
    
init()
