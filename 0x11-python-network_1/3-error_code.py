#!/usr/bin/python3
"""
Script that takes url and prints error if exists
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as elo:
            print(elo.read().decode("utf-8", "decode"))
    except as urllib.error.HTTPError as boss:
        print("Error code: {}".format(boss.code))
