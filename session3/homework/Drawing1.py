from turtle import *

speed(0)
color("grey")
for i in range(7):
    forward(100)
    left(180-900/7)

color("yellow")
for i in range(6):
    forward(100)
    left(60)

color("brown")  
for i in range (5):
    forward(100)
    left(72)

color("blue")
for i in range(4):
    forward(100)
    left(90)

color("red")
left(60)
forward(100)
right(120)
forward(100)
right(120)

color("grey")
forward(100)


mainloop()