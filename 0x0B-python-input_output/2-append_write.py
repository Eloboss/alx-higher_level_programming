#!/usr/bin/python3
"""append a file"""


def append_write(filename="", text=""):
    """returns an appended file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
