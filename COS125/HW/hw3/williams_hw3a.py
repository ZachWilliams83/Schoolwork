# File: Williams_hw3a.py
# Author: Zach Williams
# Date: 10/3/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program asks user for a number or to end the loop and returns the largest number entered.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff

def main():
    num = 0
    numlist = [0]
    #Loop to iterate through list
    for i in numlist:
        num = (input("Enter a number (or 'end' to end): "))
        # Conditional for the end condition to exit loop.
        if num == 'end':
            print(f"The largest number is {max(numlist)}")
        # Conditional for a number entered to cast as integer and append to list.
        else:
            num = int(num)
            numlist.append(num)
main()



