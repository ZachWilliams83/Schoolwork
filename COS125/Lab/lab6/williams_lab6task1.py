import random
numlist = []
newList = []
def buildRandomList(n, r):
    for i in range(n):
        num = random.randint(1,r)
        numlist.append(num)
    return(numlist)
def pruneList(r,numlist):
    for i in range(r):
        if numlist[i] not in newList:
            newList.append(numlist[i])
    return(newList)
def removeAll(numlist, e):
    for x in range(len(numlist)):
        if e in numlist:
            numlist.remove(e)
    return(numlist)
def main():
    size = int(input("What is the list size? "))
    max = int(input("What is the max number for the random numbers generated? "))
    buildRandomList(size,max)
    pruneList(size,numlist)
    print(numlist)
    print(newList)
    removeAll(numlist,2)
    print(numlist)
main()