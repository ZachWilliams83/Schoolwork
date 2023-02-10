# File: Williams_hw3c.py
# Author: Zach Williams
# Date: 10/5/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program iterates through a list and prints the index followed by the contents of that index.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff

def main():
    #Init list
    myList = ["Dog", "Cat", "Frog", "Turtle", "Horse", "Lizard", "Snake"]
    print("The pets list is: ")
    #iterate the length of the list
    for i in range(len(myList)):
        #print the index followed by the content of that index
        print(f"{i}: {myList[i]}")
        #prints the middle of that list by calling the length integer divided by 2.
    print(f"My favorite is {myList[len(myList)//2]}")
main()
