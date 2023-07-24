from turtle import *
from random import randint
speed(0)
bgcolor("black")
c=1
while(c<=200):
	r=randint(0,255)
	g=randint(0,255)
	b=randint(0,255)
	colormode(255)
	pencolor(r,g,b)
	fd(50+c)
	rt(90.911)
	c+=1
exitonclick()
	