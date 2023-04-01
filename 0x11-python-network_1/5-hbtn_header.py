#!/usr/bin/python3
"""Script that gets the header Variable"""


import requests
import sys

if __name == "__main__":
    elo = requests.get(sys.argv[1])
    boss = elo.headers.get('X-Request-Id')
    print(boss)
