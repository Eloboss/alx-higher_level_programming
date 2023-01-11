#!/usr/bin/python3
"""json representation"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
