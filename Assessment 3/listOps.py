
# A list for the task 1 - task 5
myList =[11,88,66,44,55,33,77,22,99]


# Task 1: using for loop to add all numbers in the list together
total = 0
for i in myList:
	total += i
print(total)

# Task 2: using while loop to add all numbers together
i = 0
while i != len(myList):
	total += myList[i]
	i += 1
print(total)

# Task 3:  using for loop or while loop to add only numbers in the odd positions
for i in range(0, len(myList)):
	if i%2 == 0:
		total += 0
	else:
		total += myList[i]
print(total)

# task 4: reverse the order of the list without using any built-in functions
totalLen = len(myList)
newList = []
for i in range(totalLen-1, -1, -1):
	data = myList[i]
	newList += [data]
print(newList)

# Task 5: sort the list in descending order without using any built-in functions
decNewList = []
for i in range(0, len(myList)):                     #FIX
	lastData = myList[i-1]
	data = myList[i]
	if data > lastData:
		decNewList[len(decNewList)-1] = data
		decNewList += [lastData]
	else:
		decNewList += [data]
print(decNewList)

# Task 6: check if the list is symmetrical.
# Test it by using both symmetrical and non-symmetrical lists below:
# Test data 1: myList=[11,22,33,44,44,33,22,11]
# Test data 2: myList=[11,22,33,44,33,22,11]
# Test data 3: myList=[11,33,33,44,33,22,11]



