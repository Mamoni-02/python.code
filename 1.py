import turtle
turtle.bgcolor("white")

squary = turtle.Turtle()
squary.speed(20)
squary.pencolor("blue")
for i in range(200):
    squary.forward(i)
    squary.left(50)