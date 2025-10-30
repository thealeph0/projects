import math

class Circle: #defining Circle to be a data type
    #Model a simple circle.  Each circle has a center and a radius.
    #Center is defined by x and y coordinate.
    
    #default circle
    def __init__(self, x=0, y=0, radius = 1):
        self.__x = x
        self.__y = y
        self.__radius = radius
     
    def get_radius(self): return self.__radius
    
    def get_x(self): return self.__x
    
    def get_y(self): return self.__y
    
    def get_area(self): return self.__radius**2 * math.pi
    
    def get_perimeter(self): return 2 * math.pi * self.__radius
    
    def contains(self, other_circle): ##return T/F is one circle is contained in other
        distance_squared = ((self.__x - other_circle.__x) ** 2 + (self.__y - other_circle.__y) ** 2)
        distance = math.sqrt(distance_squared)
        return distance + other_circle.__radius <= self.__radius
    
    def __str__(self):
        return ('x: ' + str(self.__x) + ", y: " + str(self.__y) + ', radius=' + str(self.__radius))
    
c1 = Circle(1,2,4)

print(str(c1))

set1 = {c1 , Circle(3,4,5)}

print(set1)

print(type(c1))
    