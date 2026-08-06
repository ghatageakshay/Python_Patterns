import turtle

screen = turtle.Screen()
screen.bgcolor('black')

star = turtle.Turtle()
star.speed(1)
colors = ["red","green","yellow","purple","blue","white"]
for i in range(6):
   
    star.color(colors[i%len(colors)])
    star.forward(160)
    star.right(144)

star.hideturtle()
screen.exitonclick()