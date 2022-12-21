#!/usr/bin/python3
"""Define a square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """square with attributes
        args:
            size: lengthof square
        """
        self.size = size

    @property
    def size(self):
        """To retrieve d size."""
        return self.__size

    @size.setter
    def size(self, value):
        """To set d attributes
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

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
