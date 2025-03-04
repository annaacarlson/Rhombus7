import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('yellow')

t = turtle.Turtle()



t.fillcolor("cyan")
t.begin_fill()
t.setheading(135)
t.forward(100)
t.setheading(225)
t.forward(100)
t.setheading(315)
t.forward(100)
t.setheading(45)
t.forward(100)
t.end_fill()

t.penup()
t.goto(0,0)
t.pendown()

t.fillcolor("brown")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()



t.hideturtle()


turtle.done()