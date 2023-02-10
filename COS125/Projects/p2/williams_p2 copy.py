from graphics import *
from random import randint
lengthWin = 800
widthWin = 800
def widthLength(aRect):
    p1 = aRect.p1.x
    p2 = aRect.p2.x
    width = p1 - p2
    p3 = aRect.p1.y
    p4 = aRect.p2.y
    length = p3 - p4
    return width, length
def splitFunc(win, numRect, colorChance, colorList, splitChance,width,length):
    x1 = 600
    x2 = 0
    y1 = 0
    y2= 600
    for i in range(numRect):
        if width >= (widthWin/2):
            splitPercent = float(randint(31,68) / 100)
            x1 = x1 * splitPercent
            y2 = y2 * splitPercent
            splitRect = Rectangle(Point(x1,y1), Point (x2,y2))
            width, length = widthLength(splitRect)
            splitRect.setOutline('black')
            splitRect.setFill(colorList[colorChance])
            splitRect.draw(win)
        elif (90 < width < (widthWin/2)):
            if splitChance < width:
                splitPercent = float(randint(31,68) / 100)
                x1 = x1 * splitPercent
                y2 = y2 * splitPercent
                splitRect = Rectangle(Point(x1, y1), Point (x2, y2))
                width, length = widthLength(splitRect)
                splitRect.setOutline('black')
                splitRect.setFill(colorList[colorChance])
                splitRect.draw(win)
            else:
                win.getMouse()
        elif 90 >= width:
            win.getMouse() # pause for click in window
    for j in range(numRect):
        if length >= (lengthWin/2):
            splitPercent = float(randint(31,68) / 100)
            x2 = x2 * splitPercent
            y1 = y1 * splitPercent
            splitRect = Rectangle(Point(x1,y1), Point (x2,y2))
            width, length = widthLength(splitRect)
            splitRect.setOutline('black')
            splitRect.setFill(colorList[colorChance])
            splitRect.draw(win)
        elif (90 < length < (lengthWin/2)):
            splitPercent = float(randint(31,68) / 100)
            x2 = x2 * splitPercent
            y1 = y1 * splitPercent
            splitRect = Rectangle(Point(x1, y1), Point (x2, y2))
            width, length = widthLength(splitRect)
            splitRect.setOutline('black')
            splitRect.setFill(colorList[colorChance])
            splitRect.draw(win)
        elif 90 >= length:
            win.getMouse() # pause for click in window
            win.close()
   
def main():
    lengthWin = 800
    widthWin = 800
    win = GraphWin("My Drawing", widthWin, lengthWin)
    counter = 0
    x1 = 600
    x2 = 0
    y1 = 0
    y2= 600
    width = 1
    length = 1
    colorChance = randint(0,4)
    colorList = ['red', 'white', 'blue','yellow','']
    aRect = Rectangle(Point(x1,y1), Point (x2,y2))
    width, length = widthLength(aRect)
    splitChance = randint(90,(width*1.5))
    aRect.setOutline("black")
    aRect.setFill('white')
    aRect.draw(win)
    splitFunc(win,20,colorChance,colorList,splitChance,width,length)
    win.getMouse()
main()
