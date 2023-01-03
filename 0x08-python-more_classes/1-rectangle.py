#!/usr/bin/python3
"""Define a Rectangle"""


class Rectangle:
    """Represent a Rectangle"""
    def __init__(self, width=0, height=0):
        """Rectangle with attributes
        args:
            width: Width of d rectangle
            height: height of d rectangle
        """
        self.width = width
        self.height = height

    @property:
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter:
    def width(self, value):
        """set d width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        else:
            return self.__width = value

    @property:
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter:
    def height(self, value):
        """set d height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        else:
            return self.__height = value
