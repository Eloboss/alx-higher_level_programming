#!/usr/bin/python3
"""Define a Rectangle"""


class Rectangle:
    """Represent a Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Rectangle with attributes
        args:
            width: Width of d rectangle
            height: height of d rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set d width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set d height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """prints d rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        return ((('#' * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """returns a message when a rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
