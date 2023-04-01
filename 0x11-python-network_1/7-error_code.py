#!/usr/bin/python3
"""Script tgat takes url and gives an error code if exists"""


if __name__ == "__main__":
    import requests
    import sys

    elo = requests.get(sys.argv[1])
    if elo.status_code >= 400:
        print('Error code: {}'.format(elo.status_code))
    else:
        print(elo.text)
