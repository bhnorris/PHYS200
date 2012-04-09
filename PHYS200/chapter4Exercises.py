"""

Code from Chapter 4 
Think Python: An Introduction to Software Design
Allen B. Downey

"""

from TurtleWorld import *
import math

def square(t, length):
    """Use the Turtle (t) to draw a square with sides of
    the given length.  Returns the Turtle to the starting
    position and location.
    """
    for i in range(4):
        fd(t, length)
        lt(t)

def polyline(t, n, length, angle):
    """Draw n line segments with the given length and
    angle (in degrees) between them.
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    """Draw regular polygon of sides specified by n 
    and length of sides by length
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """Draw an arc segment, using a linear approximation,
    of radius r and angle of the arc length by angle 
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before the polyline reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

def circle(t, r):
    """Draw a circle using the arc function's linear approximation
    to draw a full circle of 360 degrees
    """
    arc(t, r, 360)

# _main_ ==> bob = Turtle()
#        ==> r = radius
# _polyline_ ==> t = bob
#            ==> n = int(2 * math.pi * radius / 4) + 1
#            ==> length = 2 * math.pi * r / n
#            ==> angle = float(360) / int(2 * math.pi * radius / 4) + 1
# _arc_ ==> t = bob
#       ==> 


def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)

def flower(t, r, n, angle):
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)

def isosceles(t, r, alpha):
    y = r * math.sin(alpha * math.pi / 180)

    rt(t, alpha)
    fd(t, r)
    lt(t, 90 + alpha)
    fd(t, 2 * y)
    lt(t, 90 + alpha)
    fd(t, r)
    lt(t, 180 - alpha)

def piePolygon(t, n, r):
    beta = 360.0 / n
    for i in range(n):
        isosceles(t, r, beta / 2)
        lt(t, beta)

