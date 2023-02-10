# File: Williams_hw2c.py
# Author: Zach Williams
# Date: 09/16/22
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program gives simple recycling advice based on conditionals of inputs.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff

print("Welcome to the recycling coach!")
used = int(input("How many bottles / cans did you use today? "))
recycled = int(input("How many did you recycle? "))
difference = used - recycled
# Conditionals for the difference in recycled bottles / cans.
if difference > 0:
    print("You should try to recycle all bottles used!")
elif difference == 0:
    print("Good job recycling all your cans / bottles!")
elif difference < 0:
    print("Wow! Congratulations on being proactive and recycling for others!")
# Conditionals for not using or excessive use of bottles / cans.
if used == 0:
    print("Great job not using plastic bottles!")
elif used > 3:
    print("You should probably invest in a reusable bottle.")
print("Remember to visit the SCIS Help Center in Boardman 138 for help!")