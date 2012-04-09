from chapter5Exercises import *

def area(radius):
    temp = math.pi * radius**2
    return temp

def compare(x, y):
    if x > y:
        return 1
    else:
        if x == y:
            return 0
        else:
            if x < y:
                return -1

def hypotenuse(x, y):
    xy = x**2 + y**2
    h = math.sqrt(xy)
    return h

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def area(radius):
    temp = math.pi * radius**2
    return temp

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

def isBetween(x, y, z):
    if ((x <= y) and (y <= z)):
        return True
    else:
        return False

def ack(m, n):
    if m == 0:
        return n + 1
    elif ((m > 0) and (n == 0)):
        return ack(m - 1, 1)
    else:
        if ((m > 0) and (n > 0)):
            return ack(m - 1, ack(m, n - 1))

 
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def isPalindrome(string):
    if first(string) == last(string):
        if (len(middle(string)) < 2):
            return True
        else:
             return isPalindrome(middle(string))
    else:
        return False

def isPower(a, b):
    if a == 1 or a == 0 or b == 1 or b == 0:
        print "No! bad user"
        return None
    if a % b != 0:
        return False
    else:
        if not(a == b):
            if a % b == 0 and isPower(float(a) / b, b):
                return True
            else:
                return False
        else:
            return True

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

