import turtle
from turtle import *


left(90)
penup()
backward(200)



pendown()
pensize(10)
pencolor('black')
forward(400)
speed(0)
for i in range(36):
	pencolor('blue')
	forward(50)
	backward(50)
	right(10)
	pencolor('red')
	forward(100)
	backward(100)
	pencolor('blue')
	forward(50)
	backward(50)

hideturtle()





done()