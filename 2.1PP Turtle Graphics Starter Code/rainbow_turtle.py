"""
KIT101 2.1PP Turtle Graphics

Turtle Graphics task to read some existing code that uses a
predefined class (the turtle graphics device) and then to modify
the code to change the colour of each shape that the turtle draws.
"""

__author__ = "YOUR NAME"

import turtle as t

def main():
    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    t.speed(3)

    t.penup()
    t.left(135)
    t.forward(310)
    t.right(135)
    t.pendown()
    t.forward(100)
    t.right(90)

    # Joining multiple arguments together for printing can be
    # achieved by comma separating them. Note that the print
    # function will automatically insert spaces between each
    # argument.
    print("Just for your information, the Turtle is now",
          "located at", t.pos(), "and",
          "pointing at an angle of", t.heading(), "degrees.")

    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(180)
    t.penup()
    t.forward(350)
    t.left(90)
    t.pendown()
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.penup()
    t.forward(300)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.penup()
    t.forward(240)
    t.pendown()
    t.right(45)
    t.forward(150)
    t.penup()
    t.right(135)
    t.forward(105)
    t.pendown()
    t.right(135)
    t.forward(150)

    # Avoid closing the window automatically
    t.mainloop()


if __name__ == "__main__":
      main()
