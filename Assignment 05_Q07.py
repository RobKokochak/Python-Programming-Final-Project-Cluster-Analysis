#Rob Kokochak

import turtle
import random

angle = random.randint(15,45)

def tree(t, trunkLength):
    if trunkLength < (angle/5):     #check for base case
        t.pencolor("green")
        t.dot()
        return
    else:
        t.forward(trunkLength)
        t.right(angle)
        tree(t, trunkLength - (random.randint(5,25)))
        t.left(angle*2)
        tree(t, trunkLength - random.randint(5,25))
        t.right(angle)
        t.pencolor("brown")
        t.backward(trunkLength)

import turtle
t = turtle.Turtle()
t.up()
t.right(90)
t.forward(300)
t.left(180)
t.down()
trunkLength = 100
t.speed(0)
t.pencolor("brown")
tree(t, trunkLength)
