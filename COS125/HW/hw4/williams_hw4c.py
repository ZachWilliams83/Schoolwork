# File: Williams_hw4c.py
# Author: Zach Williams
# Date: 10/14/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program asks user for parameters to sing a song having to do with the inputs as arguments.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff

def singVerse(num,food):
    for i in range(num,0,-1):
        print(f"{i} bottles of {food} on the wall, {i} bottles of {food}, Take one down, pass it around, {i-1} bottles of {food} on the wall.")
    else:
        print(f"Oh no. the {food} is all gone!")
def main():
    foodInput = input("What is your favorite Maine food? ")
    numInput = int(input("How many verses? "))
    singVerse(numInput,foodInput)
main()
