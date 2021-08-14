import turtle
flag=turtle.Turtle()
flag.speed(5)
flag.pensize(7)
flag.color('blue')

def draw(x,y):
    flag.penup()
    flag.goto(x,y)
    flag.pendown()

for i in range(24):
    flag.forward(90)
    flag.backward(90)
    flag.left(15)
draw(0,-90)

flag.circle(90,360)

flag.color('green')
flag.begin_fill()
flag.forward(412)
flag.backward(824)
flag.right(90)
flag.forward(180)
flag.left(90)
flag.forward(824)
flag.left(90)
flag.forward(180)
flag.left(90)
flag.end_fill()


flag.color('orange')
draw(-412,100)

flag.begin_fill()
flag.right(180)
flag.forward(824)
flag.left(90)
flag.forward(180)
flag.left(90)
flag.forward(824)
flag.left(90)
flag.forward(180)
flag.end_fill()


turtle.done()
    