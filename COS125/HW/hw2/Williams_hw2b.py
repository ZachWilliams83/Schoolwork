# File: Williams_hw2b.py
# Author: Zach Williams
# Date: 09/16/22
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program grabs and evaluates total grades as weighted by the course instructor.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff

print("Hello, I will calculate your grade. Please only enter numbers.")
hw_weight = float(input("What is the homework weight? "))
hw_grade = float(input("What is your homework grade? "))
proj_weight = float(input("What is the project weight? "))
proj_grade = float(input("What is your project grade? "))
lab_weight = float(input("What is the lab weight? "))
lab_grade = float(input("What is your lab grade? "))
engage_weight = float(input("What is the engagement activities weight? "))
engage_grade = float(input("What is your engagement grade? "))
exam_weight = float(input("What is the hourly exam weight? "))
exam_grade = float(input("What is your hourly exam grade? "))
final_weight = float(input("What is the final exam weight? "))
final_grade = float(input("What is your final exam grade? "))
# Arithmetic for calculating total grade with weights.
total_grade = (hw_weight * hw_grade) + (proj_weight * proj_grade) + (lab_weight * lab_grade) + (engage_weight * engage_grade) + (exam_weight * exam_grade) + (final_weight * final_grade)
print("Your total grade so far is : ",total_grade)