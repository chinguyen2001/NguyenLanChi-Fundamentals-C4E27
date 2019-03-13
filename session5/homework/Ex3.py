from turtle import *

def draw_squares(length,colors):
    color(colors)
    for i in range(4):
        forward(length)
        left(90)
    mainloop()

draw_squares(100,"cyan")

