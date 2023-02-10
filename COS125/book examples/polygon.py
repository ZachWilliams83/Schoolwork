import turtle
import math
bob = turtle.Turtle()
print(bob)
length = 0
n = 7
def square(t, length):
    for i in range(4):
        length = 300
        bob.fd(length)
        bob.lt(90)
def polygon(t, length, n):
    angle = 360/n
    for i in range(n):
        n = 5
        length = 10
        bob.fd(length)
        bob.lt(angle)
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length,n)
#polygon(bob, length, n)
circle(2, 20)
turtle.mainloop()