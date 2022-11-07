import turtle
turtle.tracer(0)
k = 20
for i in range(15):
 turtle.goto(turtle.xcor()+5*k, turtle.ycor()+5*k)
 turtle.goto(turtle.xcor()+5*k, turtle.ycor()-5*k)
 turtle.goto(turtle.xcor()-5*k, turtle.ycor()-5*k)
 turtle.goto(turtle.xcor()-5*k, turtle.ycor()+5*k)
turtle.up()
for i in range(-30, 30):
 for j in range(-30,30):
    turtle.goto(i*k, j*k)
    turtle.dot(4)
turtle.update()
turtle.mainloop()