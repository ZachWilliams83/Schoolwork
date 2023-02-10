import random
def minmax(numList):
    maximum = numList[0]
    minimum = numList[0]
    for x in numList:
        if x > maximum:
            maximum = x
    for y in numList:
        if y < minimum:
            minimum = y
    return maximum, minimum
def main():
    mylist = []
    for i in range(10):
        mylist.append(random.randint(0,50))
    print(mylist)
    maximum1, minimum1 = minmax(mylist)
    print(maximum1, minimum1)
main()

