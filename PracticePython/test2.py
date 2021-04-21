# 거북이

from turtle import *
from random import *

def screenLeftClick(x, y) :
    pencolor('red')
    pendown()
    goto(x, y)

def screenMidClick(x, y) :
    pencolor('green')
    penup()
    goto(x, y)

def screenRightClick(x ,y) :
    pSize = random.randrange(10,15)
    shapesize(pSize)
    goto(x,y)

pSize = 10
title("turtle")
shape('turtle')
pensize(10)

onscreenclick(screenLeftClick, 1)
onscreenclick(screenMidClick, 2)
onscreenclick(screenRightClick, 3)




done()
