import random
myList = []
for i in range(1000):
    myList.append(random.randint(-10, 10))
final = sum(myList) / len(myList)
print("The average of 1000 random numbers between -10 and 10 is " + str(final))