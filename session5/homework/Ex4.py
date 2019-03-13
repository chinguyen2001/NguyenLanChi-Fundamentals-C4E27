from turtle import *

def draw_squares(length,colors):
    color(colors)
    for i in range(4):
        forward(length)
        left(90)
    mainloop()

for i in range(30):
    draw_squares(i*5, 'red')
    left(17)
    penup()
    forward(i*2)
    pendown()

# lol what do you mean by this exercise... it makes me feel like i have done sth wrong smh