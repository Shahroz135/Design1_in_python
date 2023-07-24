from turtle import *
from random import randint
speed(0)
bgcolor("black")
a=1
while a<=250:
	r=randint(0,255)
	g=randint(0,255)
	b=randint(0,255)
	colormode(255)
	pencolor(r,g,b)
	fd(50+a)
	rt(140)
	a+=1
exitonclick()