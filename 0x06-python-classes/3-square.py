#!/usr/bin/python3
"""Define a square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """square with attributes
        args:
            size: lengthof square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
    
    def area(self):
        """Returns area of a square"""
        return size ** 2