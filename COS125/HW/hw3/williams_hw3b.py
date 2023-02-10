# File: Williams_hw3b.py
# Author: Zach Williams
# Date: 10/5/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program asks user for 2 years to use as range for printing the years between and also evaluates for if it is a leap year.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff

def main():
    first_year = int(input("Please enter the first year: "))
    second_year = int(input("Please enter least year: "))
    #end condition for range is second year +1 because range is not inclusive in its end.
    for i in range(first_year,(second_year+1)):
        if (i % 4 == 0) and (i % 100 != 0):
            print(f"{i} is a leap year!")
        elif (i % 400 == 0) and (i % 100 == 0):
            print(f"{i} is a leap year!")
        else:
            print(i)
main()