#!/usr/bin/python3
"""search for a file and input a string"""


def append_after(filename="", search_string="", new_string=""):
    """search for a file and input a string
    args:
        search_string= string to be searched for
        new_string = string to b inputted
        filename = name of file
    """
    text = ""
    with open(filename) as boss:
        for line in boss:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as elo:
        elo.write(text)
