import turtle

s = turtle.Screen()
s.bgcolor('black')
s = turtle.Screen()
s.bgcolor('black')
t = turtle.Turtle()
t.speed(4)
turtle.delay(15)
t.color('pink')
for _ in range(6):
    t.circle(60, 60)
    t.left(120)
    t.circle(60, 60)
    t.left(60)

t.penup(); t.goto(0, -30); t.pendown()
t.color('yellow'); t.begin_fill()
t.circle(30); t.end_fill()

s.exitonclick()