from graphics import *
import random
win = GraphWin("Mondrian Art", 500, 500)

def generate_mondrian(win, num_squares):
    colors = ["red", "yellow", "blue"] # colors used in Mondrian's art

    # randomly choose colors for each square
    for i in range(num_squares):
        color = random.choice(colors)
        x1 = random.randint(0, 500) # x coordinate of top left corner
        y1 = random.randint(0, 500) # y coordinate of top left corner
        x2 = random.randint(x1, 500) # x coordinate of bottom right corner
        y2 = random.randint(y1, 500) # y coordinate of bottom right corner

        # create square with randomly chosen colors and coordinates
        square = Rectangle(Point(x1, y1), Point(x2, y2))
        square.setFill(color)
        square.draw(win)

    # split squares at random intervals
    for i in range(num_squares):
        square = random.choice(win.items[:]) # choose a random square
        x1 = square.p1.x
        x2 = square.p2.x
        y1 = square.p1.y
        y2 = square.p2.y

        # split square horizontally
        if random.random() > 0.5:
            split_point = random.randint(x1, x2)
            square1 = Rectangle(Point(x1, y1), Point(split_point, y2))
            square1.setFill(color)
            square1.draw(win)

            square2 = Rectangle(Point(split_point, y1), Point(x2, y2))
            square2.setFill(color)
            square2.draw(win)

        # split square vertically
        else:
            split_point = random.randint(y1, y2)
            square1 = Rectangle(Point(x1, y1), Point(x2, split_point))
            square1.setFill(color)
            square1.draw(win)

            square2 = Rectangle(Point(x1, split_point), Point(x2, y2))
            square2.setFill(color)
            square2.draw(win)

    # create vertical and horizontal lines
    for i in range(num_squares):
        x1 = random.randint(0, 500)
        y1 = random.randint(0, 500)
        x2 = random.randint(0, 500)
        y2 = random.randint(0, 500)

        line = Line(Point(x1, y1), Point(x2, y2))
        line.setWidth(3)
    win.getMouse()
generate_mondrian(win,10)
