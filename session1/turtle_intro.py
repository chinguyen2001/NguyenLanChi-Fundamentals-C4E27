from turtle import *

shape("turtle")
# speed(0)
color("red", "purple")

begin_fill()
for i in range(10):
    forward(50)
    pu()
    forward(50)
    pd()
    left(90)
end_fill()


mainloop()