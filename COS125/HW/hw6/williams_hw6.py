# File: Williams_hw6.py
# Author: Zach Williams
# Date: 10/24/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description: Program generates an adjacency matrix and adjacency list based on parameter set by the user.
# Collaboration:
# I collaborated with Zach Hamilton.
import random
def generateAdjMatrix(vertInput, userProb):
    #Initialize basic matrix
    adjMatrix = [[] for x in range(vertInput)]
    for i in range (vertInput):
        for j in range(vertInput):
            #conditional for whether or not a node is present
            if userProb > random.random() and i != j:
                adjMatrix[j].append(1)
            else:
                adjMatrix[j].append(0)
    return adjMatrix

def createAdjList(adjMatrix):
    adjList = [[] for x in range(len(adjMatrix))]
    for i in range(len(adjMatrix)):
        for j in range(len((adjMatrix[i]))):
            if adjMatrix[i][j] == 1:
                adjList[i].append(j)
    return adjList

def printAdjMatrix(adjMatrix):
    print("Adjacency Matrix: ")
    header = 0
    row = 0
    x = 0
    #spacer
    print("  ", end = "")
    while header < len(adjMatrix):
        print(header, end = " ")
        header +=1
    print()
    #Cleaning up the matrix data
    for i in adjMatrix:
        print(x, end= " ")
        row = str(i)
        row = row.replace(',','')
        row = row.replace('[','')
        row = row.replace(']','')
        print(row)
        x += 1
    print()
def printAdjList(adjList):
    x = 0
    rowline = ''
    print("Adjacency List:")
    #Iterate through each row to find nodes and print cleaned up.
    for p in adjList:
        print(x, end= ': ')
        rowline = str(p)
        rowline = rowline.replace('[','')
        rowline = rowline.replace(']','')
        print(rowline)
        x+= 1
    print()

def main():
    userProb = 2
    vertInput = int(input("What is the number of vertices in the graph? "))
    while userProb < 0 or userProb > 1:
        userProb = float(input("What is the probability that there is an edge from one node to another? "))
        if userProb < 0 or userProb > 1:
            print("userProb must be between 0 and 1.")
    matrix = generateAdjMatrix(vertInput,userProb)
    userlist = createAdjList(matrix)
    printAdjMatrix(matrix)
    printAdjList(userlist)
main()
#Sample output for 5 vert, .25 prob
# Adjacency Matrix: 
#   0 1 2 3 4 
# 0 0 0 0 0 0
# 1 0 0 0 0 0
# 2 0 1 0 0 0
# 3 0 0 0 0 0
# 4 0 0 0 0 0

# Adjacency List:
# 0:
# 1:
# 2: 1
# 3:
# 4:
