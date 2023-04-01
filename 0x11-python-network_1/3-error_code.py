#!/usr/bin/python3
"""
Script that takes url and prints error if exists there is error
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as elo:
            print(elo.read().decode("utf-8"))
    except as urllib.error.HTTPError as boss:
        print("Error code: {}".format(boss.code))
