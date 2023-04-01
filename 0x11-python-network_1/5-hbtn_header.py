#!/usr/bin/python3
"""Script that gets the header Variable"""


if __name__ == "__main__":
    import requests
    import sys

    elo = requests.get(sys.argv[1])
    boss = elo.headers.get('X-Request-Id')
    print(boss)
