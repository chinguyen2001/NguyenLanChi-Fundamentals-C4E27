# Hình 1

from turtle import *

speed(0)
color("red")

for i in range(4):
    forward(50)
    right(60)
    forward(50)
    right(120)
    forward(50)
    right(60)
    forward(50)
    right(30)

mainloop()


# Hình 2


from turtle import *

speed(0)
color("red")

for i in range(4):
    forward(100)
    left(90)

for i in range(6):
    forward(100)
    left(60)

color("blue")

pu()
forward(100)
pd()

for i in range (4):
    left(72)
    forward(100)

left(132)
forward(100)
right(120)
forward(100)


mainloop()