#!/usr/bin/python3
"""Define a square."""


class Square:
    """Represent a Square."""
    def __init___(self, size=0):
        """square attributes"""
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
