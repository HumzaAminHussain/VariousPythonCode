import turtle
turtle.pencolor('blue')
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.right(90)
turtle.forward(50)
turtle.reset()
turtle.penup()
turtle.goto(0,-275)
turtle.pendown()
turtle.pencolor('blue')
turtle.fillcolor('blue')
turtle.begin_fill()
radius =  turtle.numinput('radius needed ', 'enter the radius')
turtle.circle(radius)
turtle.end_fill()
turtle.done()