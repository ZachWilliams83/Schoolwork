# File: Williams_hw1c.py
# Author: Zach Williams
# Date: 09/09/22
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program receives input of a number and displays the square and cube of the number.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff

num = input("Enter a number: ")
num = int(num)
square = num ** 2
square = str(square)
cube = num ** 3
cube = str(cube)
print("The square is: "+square)
print("The cube is: "+cube)