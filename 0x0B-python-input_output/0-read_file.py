#!/usr/bin/python3
"""input and otput file"""


def read_file(filename=""):
    """prints a read file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
