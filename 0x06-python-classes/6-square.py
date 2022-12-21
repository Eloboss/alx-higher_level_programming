#!/usr/bin/python3
"""Define a square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """square with attributes
        args:
            size: length of square
            position: positioning of d square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """To retrieve d size."""
        return self.__size

    @size.setter
    def size(self, value):
        """To set d size
        args:
            value: size of d square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """To retrieve d position."""
        return self.__position

    @position.setter
    def position(self, value):
        """To set d position
        args:
            value: size of d square
        """
        if type(value) is not tuple or len(value) != 2\
           or type(value[0]) is not int or type(value[1]) is not int\
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        " ""Returns area of square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints d square with a #."""
        if self.__size == 0:
            print()
        else:
            string = '#' * self.__size
            margin = ' ' * self.__position[0]
            for x in range(self.__size):
                print(margin, string, end="")
