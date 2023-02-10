# File: Williams_hw5a.py
# Author: Zach Williams
# Date: 10/17/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program asks user how many slogans they want created, and a randomly generated
# pseudo-political slogan is created based on pre - established lists.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff
import random

def sloganGen():
    name = ['Hulk', 'Spock', 'Ted Lasso', 'Aaron Burr', 'The Cowardly Lion', 'Cinderella',
    'Black Panther', 'Merida', 'Uhuru', 'Freya', 'Frodo', 'Megan Rapinoe']
    verbs = ['Serving', 'Building', 'Creating', 'Putting', 'Fighting', 'Taking', 'Cleaning up', 
    'Protecting', 'Putting', 'Smashing', 'Working', 'Coaching', 'Kicking']
    directObjects = ['the future', 'our community', 'jobs', 'education', 'corruption', 
    'action', 'families', 'change', 'progress', 'government', 'results', 'our enemies']
    adverbs = [ 'with integrity', 'for you', 'first', 'safe', 'for the future', 'for a change', 
    'for Maine', 'with experience', 'with vision']
    # Print statement for random list values of each list to create a slogan.
    print(f"{name[random.randint(0,11)]}: {verbs[random.randint(0,12)]} {directObjects[random.randint(0,11)]} {adverbs[random.randint(0,8)]}")
def main():
    num = int(input("How many slogans would you like? "))
    for i in range (num):
        sloganGen()
main()