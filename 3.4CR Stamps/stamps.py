__author__ = "Blake Natoli"

import turtle as t
from math import sqrt, atan, degrees

SQRT_2 = 1.4142135623730951

def place_stamp(stamper, x: float, y: float, color=(0,0,0), size=1, rotation=0, speed=3) -> None:
    """
    Draws the authors initials
    """
    default_size = stamper.window_width() * 0.125
    size = round(size, 1) * default_size

    stamper.colormode(255)
    stamper.speed(speed)
    stamper.pencolor(color)

    # Moving
    stamper.seth(-rotation)
    stamper.penup()
    stamper.goto((x,y))
    stamper.right(135)
    stamper.forward((SQRT_2 * size) * 0.5)
    stamper.right(135)
    
    # B
    stamper.pendown()
    stamper.forward(size)
    stamper.right(90)
    stamper.circle(-size/4,180)
    stamper.right(180)
    stamper.circle(-size/4,180)

    # Moving
    stamper.penup()
    stamper.right(180)
    stamper.forward(size/2)
    stamper.left(90)
    
    # N
    stamper.pendown()
    stamper.forward(size)
    angle = degrees(atan(size / (size*.5)))
    stamper.right(90 + angle)
    stamper.forward(sqrt((size)**2+(size/2)**2))
    stamper.left(90 + angle)
    stamper.forward(size)
    
    stamper.penup()
    stamper.goto((0,0))
    stamper.seth(0)

def main():
    place_stamp(t,-150,150,(255,0,0), 1.5, 0, 10)
    place_stamp(t,-300,-200,rotation=45,size=2, color=(0,0,255), speed=10)
    place_stamp(t, 200, -100, color=(185, 85, 175), size=.5, rotation=-90, speed=10)

    t.mainloop()

if __name__ == "__main__":
    main()