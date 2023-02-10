# File: Williams_hw2a.py
# Author: Zach Williams
# Date: 09/16/22
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program calculates average attendance for lab meetings, as well as prints a warning for being over capacity.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff

print("Hello, I will calculate the lab attendance average.")
lab0 = float(input("What was the attendance at Lab 0? "))
lab1 = float(input("What was the attendance at Lab 1? "))
lab2 = float(input("What was the attendance at Lab 2? "))
lab3 = float(input("What was the attendance at Lab 3? "))
# Evaluate the average attendance and assign it to avg
avg = int((lab0 + lab1 + lab2 + lab3) // 4)
print("The average attendance in the first four labs was ",avg)
# Conditionals for if the room capacity is exceeded at a lab meeting
if lab0 > 20:
    print("Warning! The first lab meeting looks like it exceeded the room capacity!")
elif lab1 >20:
    print("Warning! The second lab meeting looks like it exceeded the room capacity!")
elif lab2 > 20:
    print("Warning! The third lab meeting looks like it exceeded the room capacity!")
elif lab3 > 20:
    print("Warning! The fourth lab meeting looks like it exceeded the room capacity!")

