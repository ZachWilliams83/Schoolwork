import graphics
import random

win = graphics.GraphWin("Mondrian Art", 600, 600)

# helper function to split the window into two rectangles
def split_window(win, direction):
# determine the dimensions of the window
    width = win.getWidth()
    height = win.getHeight()

# Copy code
# split the window horizontally or vertically based on the direction
    if direction == "horizontal":
        # create two rectangles with equal width
        rect1 = graphics.Rectangle(graphics.Point(0, 0), graphics.Point(width/2, height))
        rect2 = graphics.Rectangle(graphics.Point(width/2, 0), graphics.Point(width, height))
    else:
        # create two rectangles with equal height
        rect1 = graphics.Rectangle(graphics.Point(0, 0), graphics.Point(width, height/2))
        rect2 = graphics.Rectangle(graphics.Point(0, height/2), graphics.Point(width, height))

# return the two rectangles
    return rect1, rect2
#elper function to draw the rectangles and randomly split them
def draw_and_split(rectangles):
# randomly choose a rectangle to split
    rect_to_split = random.choice(rectangles)

# Copy code
# determine the dimensions of the rectangle
    width = rect_to_split.getWidth()
    height = rect_to_split.getHeight()

# if the width is greater than the height, split the rectangle horizontally
# if the height is greater than the width, split the rectangle vertically
# if the width and height are equal, randomly choose a direction to split
    if width > height:
        rect1, rect2 = split_window(rect_to_split, "horizontal")
    elif height > width:
        rect1, rect2 = split_window(rect_to_split, "vertical")
    else:
        if random.random() > 0.5:
            rect1, rect2 = split_window(rect_to_split, "horizontal")
        else:
            rect1, rect2 = split_window(rect_to_split, "vertical")

    # remove the rectangle that was split from the list of rectangles
    rectangles.remove(rect_to_split)

    # add the two new rectangles to the list of rectangles
    rectangles.append(rect1)
    rectangles.append(rect2)

    # draw the rectangles with random colors
    for rect in rectangles:
        color = random.choice(["red", "yellow", "blue", "black"])
        rect.setFill(color)
        rect.draw(win)
    #create a list of rectangles with the initial window
    rectangles = [graphics.Rectangle(graphics.Point(0, 0), graphics.Point(win.getWidth(), win.getHeight()))]

    #randomly split and draw the rectangles until there are more than 20 rectangles
    while len(rectangles) < 20:
        draw_and_split(rectangles)
draw_and_split()
win.getMouse()
win.close()