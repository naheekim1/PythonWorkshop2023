#Object Oriented Programming!!!! >:)
from math import * #Bad practice using import *

class Point:
    def __init__(self, xCoord, yCoord):
        self.__x = xCoord
        self.__y = yCoord

    def distanceToPoint(self, point2):
        return sqrt((self.__x - point2.__x)**2 + (self.__y - point2.__y)**2)
    
    def magnitude(self):
        origin = Point(0, 0)
        return self.distanceToPoint(origin)
    
    def addToY(self, num):
        self.__y += num
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, newX):
        self.__x = newX
    
    def setY(self, newY):
        self.__y = newY
    
    def __str__(self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"

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