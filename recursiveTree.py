import turtle

def tree(t, trunkLength):
    if trunkLength < 5:     #check for base case
        return
    else:
        t.forward(trunkLength)
        t.right(30)
        tree(t, trunkLength - 15)
        t.left(60)
        tree(t, trunkLength - 15)
        t.right(30)
        t.backward(trunkLength)

import turtle
t = turtle.Turtle()
t.left(90)
trunkLength = 100
t.speed(0)
tree(t, trunkLength)

