# File: Williams_hw1b.py
# Author: Zach Williams
# Date: 09/09/22
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program grabs price per candy bar and multiplies for sales tax to display final price
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff

#Get an input for price of candy bar
price = input("How much is this candy bar? ")
#Convert string to integer
price = int(price)
#Math to get final cost
total_cost = ((price * 3) * .0055) + (price * 3)
#Convert to string to concatenate final display.
total_cost = str(total_cost)
print("I would like three bars. Here is $ "+total_cost)
print("Thank you.")