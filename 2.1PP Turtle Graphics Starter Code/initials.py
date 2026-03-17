"""
KIT101 2.1PP Turtle Graphics

Turtle Graphics task to draw the author's initials.
Some of the code below has been _over_ commented to help
you understand what is happening.
"""

__author__ = "Blake Natoli"

import turtle as t
from math import degrees, acos, sqrt

def main():
    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    t.speed(3)
    t.pensize(3)

    # Draw your initials below, remembering to use painter.penup() to
    # move without drawing a line...
    
    windowWidth = t.window_width()
    windowHeight = t.window_height()
    
    t.penup()
    t.setpos((-windowWidth * .25, windowHeight * .25))
    t.seth(-90)
    t.pendown()
    
    t.forward(windowHeight * .5)
    
    for i in range (2):
        t.seth(0)
        t.circle(100, 180)
    t.penup()
    
    t.seth(0)
    t.forward(200)
    
    t.seth(-90)
    t.pendown()
    t.forward(windowHeight * .5)
    t.seth(90)
    t.penup()
    t.forward(windowHeight * .5)
    t.pendown()
    
    sideLength = 200
    
    angle = degrees(acos(sideLength / (windowHeight*.5)))
    forward = sqrt(int((windowHeight*.5) ** 2) + sideLength**2)
    
    t.right(90 + angle)
    t.forward(forward)
    
    t.seth(90)
    
    t.forward(windowHeight*.5)
    
    # Avoid closing the window automatically
    t.mainloop()


if __name__ == "__main__":
    main()
