from turtle import *
k = 40
left(90)
for i in range(7):
    forward(10 * k)
    right(120)

penup()
for x in range(11):
    for y in range(11):
        goto(x * k, y * k)
        dot(4)

mainloop()