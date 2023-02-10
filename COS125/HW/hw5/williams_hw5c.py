# File: Williams_hw5c.py
# Author: Zach Williams
# Date: 10/18/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program automates a dice game until the total reaches 20+ or the "player" rolls a 1.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff
import random

def pigGame():
    turnTotal = 0
    while turnTotal < 20:
        roll = random.randint(1,6)
        turnTotal += roll
        print(f"Roll: {roll}")
        if roll == 1:
            break
    print(f"Turn total: {turnTotal}")
def main():
    pigGame()
main()