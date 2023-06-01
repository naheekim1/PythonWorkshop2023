#Object Oriented Programming!!!! >:)
from math import * #Bad practice using import *

class Point:
    def __init__(self, xCoord, yCoord):
        self._x = xCoord
        self._y = yCoord

    def distanceToPoint(self, point2):
        return sqrt((self._x - point2._x)**2 + (self._y - point2._y)**2)
    
    def magnitude(self):
        origin = Point(0, 0)
        return self.distanceToPoint(origin)
    
    def addToY(self, num):
        self._y += num
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y
    
    def setX(self, newX):
        self._x = newX
    
    def setY(self, newY):
        self._y = newY
    
    def __str__(self):
        return "(" + str(self._x) + ", " + str(self._y) + ")"

def main():
    a = Point(4, 6)
    b = Point(1, 2)
    
    print("Point a:", a)
    print("Point b:", b)

    dist = a.distanceToPoint(b)
    a.addToY(-3)
    dist2 = a.magnitude()

    print("New and Improved point a:", a)

    print("The distance between the points is:", dist)
    print("The distance between a and the origin:", dist2)

main()