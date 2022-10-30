import turtle
from turtle import *
xw=200
xx=10
xy='black'
xz=200

state={'turn':0}
hideturtle()
pensize(20)
pencolor(xy)

def spinner():
	clear()
	angle = state['turn']/10
	right(angle)
	forward(xw)
	dot(xz,'red')
	dot(xx,xy)
	penup()
	backward(xw)
	pendown()
	right(360/7)
	forward(xw)
	dot(xz,'orange')
	dot(xx,xy)
	penup()
	backward(xw)
	pendown()
	right(360/7)
	forward(xw)
	dot(xz,'yellow')
	dot(xx,xy)
	penup()
	backward(xw)
	pendown()
	right(360/7)
	forward(xw)
	dot(xz,'green')
	dot(xx,xy)
	penup()
	backward(xw)
	pendown()
	right(360/7)
	forward(xw)
	dot(xz,'blue')
	dot(xx,xy)
	penup()
	backward(xw)
	pendown()
	right(360/7)
	forward(xw)
	dot(xz,'indigo')
	dot(xx,xy)
	penup()
	backward(xw)
	pendown()
	right(360/7)
	forward(xw)
	dot(xz,'purple')
	dot(xx,xy)
	penup()
	backward(xw)
	pendown()
	right(360/7)
	update()


def animate():
	if state['turn']>0:
		state['turn'] -=1
	spinner()
	ontimer(animate,20)

def click(x,y):
	state['turn'] +=10

setup(600,600,370,0)
tracer(False)


turtle.onscreenclick(click)
listen()
animate()
done()


