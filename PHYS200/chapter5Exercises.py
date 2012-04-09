import math
from letters import *

def checkFermat():
    promptA = "Enter first value\n"
    A = raw_input(promptA)
    promptB = "Enter Second value\n"
    B = raw_input(promptB)
    promptC = "Enter Third value\n"
    C = raw_input(promptC)
    promptN = "Enter Power value\n"
    N = raw_input(promptN)
    A = int(A)
    B = int(B)
    C = int(C)
    N = int(N)
    if ((A**N) + (B**N)) == (C**N):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

def isTriangle():
    prompt = "Enter int value\n"
    A = raw_input(prompt)
    B = raw_input(prompt)
    C = raw_input(prompt)
    A = int(A)
    B = int(B)
    C = int(C)
    if ((A > (B + C)) or (B > (A + C)) or (C > (A + B))):
        print "No"
    else:
        print "Yes"

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

def koch(t, x):
    if not(x < 3):
        koch(t, x / 3)
        lt(t, 60)
        koch(t, x / 3)
        rt(t, 120)
        koch(t, x / 3)
        lt(t, 60)
        koch(t, x / 3)
    else:
        fd(t, x)

def createWorld(t):
    world = TurtleWorld()
    t = Turtle()
    t.delay = 0.00000001

def snowflake(t, x):
    for i in range(3):
        koch(t, x)
        rt(t, 120)
    


