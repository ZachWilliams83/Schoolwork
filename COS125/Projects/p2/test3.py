import random
from graphics import *
win = GraphWin("My Drawing", 800, 800)
# Define the original rectangle
rect = Rectangle(Point(0, 0), Point(100, 100))

# Generate random coordinates for the new rectangles
x1 = random.random() * 100
y1 = random.random() * 100
x2 = random.random() * (100 - x1)
y2 = random.random() * (100 - y1)
x3 = random.random() * (100 - x1 - x2)
y3 = random.random() * (100 - y1 - y2)

# Create the new rectangles using the random coordinates
rect1 = Rectangle(Point(0, 0), Point(x1, y1))
rect2 = Rectangle(Point(x1, 0), Point(x1 + x2, y2))
rect3 = Rectangle(Point(x1 + x2, 0), Point(x1 + x2 + x3, y3))
rect4 = Rectangle(Point(0, y1), Point(x1, y1 + y2))

# Draw the rectangles on the screen
rect1.draw(win)
rect2.draw(win)
rect3.draw(win)
rect4.draw(win)
win.getMouse()
