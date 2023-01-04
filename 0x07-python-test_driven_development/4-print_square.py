#!/usr/bin/python3
"""prints a square"""


def print_square(size):
    """Square with size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    string = '#' * size
    for x in range(size):
        print(string)
