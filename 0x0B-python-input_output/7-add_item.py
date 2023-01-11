#!/usr/bin/python3
"""adds all list to a file"""


import sys
import json


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_json = __import__('6-load_from_json_file').load_from_json_file

    try:
        boss = load_json("add_item.json")
    except FileNotFoundError:
        boss = []
    boss.append(sys.argv[1:])
    save_to_json_file(boss, "add_item.json")