# File: Williams_hw4b.py
# Author: Zach Williams
# Date: 10/14/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program asks user for park opinion inputs and then asks which to celebrate
# Which then prints their faovrite thing attendance/10 times.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff
park_list = []
attend_list = []
favList = []
def main():
    park_list_input = ""
    for i in range(5):
        park_list_input = input("What is one of your favorite Maine parks? ")
        if park_list_input != 'done':
            favorite = input(f"What is your favorite thing about {park_list_input}? ")
            attendance = int(input(f"How many thousand people visit {park_list_input} in a year? "))
            park_list.append(park_list_input)
            attend_list.append(attendance)
            favList.append(favorite)
        else:
            celebrate()
def celebrate():      
    celebrate = int(input(f"Which park to celebrate (between 0 and {len(park_list)-1}? "))
    print(f"At {park_list[celebrate]}, I love the: ")
    for x in range(attend_list[celebrate]//10):
        print(favList[celebrate])
main()