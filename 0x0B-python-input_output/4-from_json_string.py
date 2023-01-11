#!/usr/bin/python3
"""json representation of python structure"""


import json


def from_json_string(my_str):
    """json representation"""
    return json.loads(my_str)
