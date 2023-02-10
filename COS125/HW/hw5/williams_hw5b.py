# File: Williams_hw5b.py
# Author: Zach Williams
# Date: 10/17/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:
# Program asks user for a name to string slice and use in the Name Game song.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff

def songGen(inputName):
    name = inputName
    cutName = name[1:]
    if (name[0:1] == 'A') or (name[0:1] == 'E') or (name[0:1] == 'I' or (name[0:1] == 'O'or (name[0:1] == 'U'))):
        print(f"{name}, {name}, bo-b{name.lower()}\n  Banana-fana fo-f{name.lower()}\n  Fee-fi-mo-m{name.lower()}\n  {name}!  ")
    elif (name[0:1] == 'B'):
        print(f"{name}, {name}, bo-{cutName}\n  Banana-fana fo-f{cutName}\n  Fee-fi-mo-m{cutName}\n  {name}!  ")
    elif (name[0:1] == 'F'):
         print(f"{name}, {name}, bo-b{cutName}\n  Banana-fana fo-{cutName}\n  Fee-fi-mo-m{cutName}\n  {name}!  ")
    elif (name[0:1] == 'M'):
         print(f"{name}, {name}, bo-b{cutName}\n  Banana-fana fo-f{cutName}\n  Fee-fi-mo-{cutName}\n  {name}!  ")
    else:
        print(f"{name}, {name}, bo-b{cutName}\n  Banana-fana fo-f{cutName}\n  Fee-fi-mo-m{cutName}\n  {name}!  ")
def main():
    inputName = ''
    while True:
        inputName = input("Name to use: ")
        if inputName == 'quit':
            break
        songGen(inputName)
main()