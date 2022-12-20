#!/usr/bin/python3
"""Define a square."""


class Square:
    """Represent a Square."""
    def __init___(self, size=0):
        """square attributes
        args:
            size: length of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
