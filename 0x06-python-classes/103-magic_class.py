#!/usr/bin/python3
"""Define a Circle"""


import math


class MagicClass:
    """Represent a Circle."""
    def __init__(self, radius):
        """Circle attributes
        args:
            radius: size of circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    
    def area(self):
        """Returns area of a circle"""
        return ((self.__radius ** 2) * (math.pi))

    def circumference(self):
        """Returns circumference of a circle"""
        return ((math.pi * 2) * (self.__radius))
