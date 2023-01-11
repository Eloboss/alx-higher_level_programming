#!/usr/bin/python3
"""input output file"""

def write_file(filename="", text=""):
    """returns awritten file"""
    with open(filename, "w", encoding="utf-8") as f:
        print(f.write(text), end="")
