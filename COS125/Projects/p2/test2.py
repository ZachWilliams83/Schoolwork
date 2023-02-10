from graphics import *
import random

win = GraphWin("Mondrian Art", 500, 500)
def generate_mondrian(win, num_squares):
    colors = ["red", "yellow", "blue"] # colors used in Mondrian's art

    # divide window into grid of squares
    square_size = 500 // num_squares
    for i in range(num_squares):
        for j in range(num_squares):
            x1 = i * square_size
            y1 = j * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size

            # create square with randomly chosen color
            square = Rectangle(Point(x1, y1), Point(x2, y2))
            square.setFill(random.choice(colors))
            square.draw(win)

    # create vertical and horizontal lines
    for i in range(num_squares):
        lineLength = random.randint(0,50)
        x1 = i * lineLength
        y1 = 0
        x2 = x1
        y2 = 500

        line = Line(Point(x1, y1), Point(x2, y2))
        line.setWidth(1)
        line.draw(win)

    for i in range(num_squares):
        x1 = 0
        y1 = i * square_size
        x2 = 500
        y2 = y1

        line = Line(Point(x1, y1), Point(x2, y2))
        line.setWidth(2)
        line.draw(win)
    win.getMouse()
generate_mondrian(win,20)