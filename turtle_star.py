import turtle

wn = turtle.Screen()
wn.bgcolor("black")
pen = turtle.Turtle()
pen.speed(1)
pen.color("cyan")
pen.pensize(2)

for _ in range(60):
    pen.forward(120)
    pen.right(170)

wn.exitonclick()
