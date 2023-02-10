# File: Williams_hw4a.py
# Author: Zach Williams
# Date: 10/13/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program asks user for 5 groups of 2 inputs with national park stats
# Program returns stats such as avg, and min / max based on list inputs.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff


park_list = []
attend_list = []
def attendMin():
    min_attend = min(attend_list)
    #F string to return the value at the index where the min was found and return the value of the min itself
    print(f"The park with the fewest visitors is {park_list[attend_list.index(min(attend_list))]} with {min_attend} thousand ")
def attendMax():
    #Same idea as above
    max_attend = max(attend_list)
    print(f"The park with the most visitors is {park_list[attend_list.index(max(attend_list))]} with {max_attend} thousand")
def attendTotal():
    #Sum function to add all iterables in the list
    print(f"The total number of visitors at those parks is {sum(attend_list)} thousand.")
def attendAvg():
    # Sum / length of list to return average WITHOUT using numpy
    avg_attend = int(sum(attend_list) / len(attend_list))
    print(f"The average number of visitors per park is {avg_attend} thousand.")
def main():
    for i in range(5):
        park_list_input = input("What is one of your favorite Maine parks? ")
        attendance = int(input(f"How many thousand people visit {park_list_input} in a year? "))
        park_list.append(park_list_input)
        attend_list.append(attendance)
    attendMin()
    attendMax()
    attendTotal()
    attendAvg()
main()
