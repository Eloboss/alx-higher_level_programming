#!/usr/bin/python3
"""returns a dictionary rep for json"""


def class_to_json(obj):
    """returns a dictionary like of an object"""
    return obj.__dict__
