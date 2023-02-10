# File: Williams_p2.py
# Author: Zach Williams
# Date: 12/9/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description:Program attempts to generate art in the style of Piet Mondrian, I ultimately failed.
# I seriously was unable to tackle this problem, I tried my hardest, but I could not figure out the math
# specifically involving geometry, this is a wake up call for sure.
# Collaboration: I collaborated with Cam Hughes.

from graphics import *
import random

# Function to determine color
def colorFunc(aRect):
    rectColor = random.random()
    if rectColor < 0.09:
        aRect.setFill("yellow")
    elif rectColor < 0.15:
        aRect.setFill("blue")
    elif rectColor < 0.25:
        aRect.setFill('red')
    else:
        aRect.setFill('white')

#width and length calculating function - to simplify
def widthLength(aRect):
    p1 = aRect.p1.getX()
    p2 = aRect.p2.getX()
    width = p1 - p2
    p3 = aRect.p1.getY()
    p4 = aRect.p2.getY()
    length = p3 - p4
    return width, length, p1, p2, p3, p4

# highly conditional function that unfortunately does not work.
def splitFunc(aRect, win, lengthWin, widthWin):
    width, length, x1, x2, y1, y2 = widthLength(aRect)
    # conditional to produce random split percentage
    if width > 90:
        randSplitW = random.randrange(90, int(width*1.5))
    if length > 90:
        randSplitL = random.randrange(90, int(length*1.5))
    #conditional to (unsuccesfully) produce randomly splitting rectangles in the style of mondrian
    if (width <= (widthWin/2) or (((90<width<widthWin/2)) and randSplitW < width)):
        splitPercent = random.randint(31, 68)
        x2 = int(x2 * splitPercent // 100)
        y1 = int(y1 * splitPercent // 100)
        y2 = int(y2 * splitPercent // 100)
        x1 = int(x1 * splitPercent // 100)
        x2 = random.random() * (800 - x1)
        y2 = random.random() * (800 - y1)
        x3 = random.random() * (800 - x1 - x2)
        y3 = random.random() * (800 - y1 - y2)
        #These were for the split rectangles, obviously some of the math is off - i don't get it.
        splitRect = Rectangle(Point(x1, y1), Point(x2, y2))
        rect1 = Rectangle(Point(x1,y1)(Point(width +x2),(width+y2)))
        rect2 = Rectangle(Point(x1,y1)(Point(width +x2),(width+y2)))
        width, length, x1, x2, y1, y2 = widthLength(splitRect)
        width, length, x1, x2, y1, y2 = widthLength(rect1)
        width, length, x1, x2, y1, y2 = widthLength(rect2)
        splitRect.setOutline('black')
        rect1.setOutline('black')
        rect2.setOutline('black')
        colorFunc(rect2)
        colorFunc(rect1)
        colorFunc(splitRect)
        rect2.draw(win)
        rect1.draw(win)
        splitRect.draw(win)
        return splitRect, rect1, rect2
        #conditional to stop the split, width-wise
    elif 90 >= width:
        win.getMouse()  # pause for click in window
        #length conditional - same as above.
    if length <= (lengthWin/2) or (((90< length < lengthWin/2) and randSplitL < length)):
        splitPercent = random.randint(31, 68)
        x2 = int(x2 * splitPercent // 100)
        y1 = int(y1 * splitPercent // 100)
        y2 = int(y2 * splitPercent // 100)
        x1 = int(x1 * splitPercent // 100)
        x2 = random.random() * (800 - x1)
        y2 = random.random() * (800 - y1)
        x3 = random.random() * (800 - x1 - x2)
        y3 = random.random() * (800 - y1 - y2)

# Create the new rectangles using the random coordinates
        rect1 = Rectangle(Point(0, 0), Point(x1, y1))
        rect2 = Rectangle(Point(x1, 0), Point(x1 + x2, y2))
        rect3 = Rectangle(Point(x1 + x2, 0), Point(x1 + x2 + x3, y3))
        rect4 = Rectangle(Point(0, y1), Point(x1, y1 + y2))
        width, length, x1, x2, y1, y2 = widthLength(rect1)
        rect2.setOutline('black')
        rect1.setOutline('black')
        rect3.setOutline('black')
        colorFunc(rect3)
        colorFunc(rect2)
        colorFunc(rect1)
        rect1.draw(win)
        rect2.draw(win)
        rect3.draw(win)
        return rect1, rect2, rect3
    elif 90 >= length:
        win.getMouse()  # pause for click in window


def main():
    lengthWin = 550
    widthWin = 550
    win = GraphWin("My Drawing", widthWin, lengthWin)
    counter = 0
    x1 = 600
    x2 = 0
    y1 = 0
    y2 = 600
    width = 1
    length = 1
    colorChance = random.randint(0, 4)
    colorList = ['red', 'white', 'blue', 'yellow', '']
    aRect = Rectangle(Point(x1, y1), Point(x2, y2))
    aRect.setOutline("black")
    aRect.setFill('white')
    aRect.draw(win)
    rect1 = splitFunc(aRect, win, lengthWin, widthWin)
    #randomly decided range to produce mondrian art
    for i in range(10):
        splitFunc(aRect, win, lengthWin, widthWin)
    win.getMouse()


main()
