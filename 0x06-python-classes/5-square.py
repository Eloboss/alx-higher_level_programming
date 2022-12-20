#!/usr/bin/python3
"""Define a square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Square witb attributes
        args:
            size: length of square
        """
        self.size = size

    @property
    def size(self):
        """To retrieve d size"""
        return self.__size

    @size.setter
    def size(self, value):
        """To set d size
        args:
            value: size of square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns area of square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints d square with a #."""
        if self.__size == 0:
            print()
        else:
            str = '#' * self.__size
            for x in range(self.__size):
                print(str)
