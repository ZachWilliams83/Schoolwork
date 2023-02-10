# File: Williams_hw3d.py
# Author: Zach Williams
# Date: 10/5/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program asks user for 2 numbers and then prints the first (second number entered) 
# multiples from 1 to the first number (inclusive) and then if the user enters a negative it prints goodbye.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff

def main():
    first_num = 1
    second_num = 0
    counter = 0
    #Conditionals for positive number
    while first_num >= 0 and second_num >= 0:
        #inputs for numbers, i originally tried to use .split() from the documentation, 
        # but it would notWork at all unless I split the variables.
        first_num = int(input("What is your first number? "))
        second_num = int(input("What is your second number? "))
        if first_num == 0:
            print("Hmm. Nothing to see here.")
        else:
            #Overall loop to make the inner loop run for 1 to x inclusive
            for j in range(1,first_num+1):
                counter = 1
                # Prints the first (second num) multiples of that number 
                # from the above loop.
                for i in range(1, second_num+1):
                    print(j*counter, end = " ")
                    counter += 1
                print("\n")
    #Negative condition.
    else:
        print("Goodbye.")
main()