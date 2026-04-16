from turtle import *

screen = Screen()
screen.title("Write Your Name")
screen.setup(width= 1000, height= 400)

pen = Turtle()
pen.speed(0)
pen.pensize(5)

#B
pen.penup()
pen.color("Blue")
pen.goto(-400,-75)
pen.pendown()
pen.left(90)
pen.forward(200)
pen.right(90)
for i in range(180):
    pen.forward(1)
    pen.right(1)
pen.right(180)
for i in range(180):
    pen.forward(1)
    pen.right(1)
pen.right(90)
pen.forward(50)
pen.penup()

#U
pen.goto(-300,0)
pen.color("green")
pen.pendown()
pen.right(180)
pen.forward(50)
for i in range(180):
    pen.forward(.5)
    pen.left(1)
pen.forward(50)
pen.penup()

#R
pen.goto(-200,0)
pen.color("orange")
pen.pendown()
pen.right(180)
pen.forward(80)
pen.right(180)
pen.forward(80)
pen.right(90)
for i in range(180):
    pen.forward(.5)
    pen.right(1)
pen.left(140)
pen.forward(40)
pen.penup()

#K
pen.goto(-125,0)
pen.color("red")
pen.pendown()
pen.left(-50)
pen.forward(75)
pen.right(180)
pen.forward(37.5)
pen.right(45)
pen.forward(40)
pen.right(180)
pen.forward(40)
pen.left(90)
pen.forward(50)
pen.penup()

#E
pen.goto(-70,-35)
pen.color("purple")
pen.pendown()
pen.setheading(0)
pen.forward(50)
pen.left(90)
pen.circle(25,180)
for i in range(90):
    pen.forward(.5)
    pen.left(1)
pen.forward(20)
screen.exitonclick()
