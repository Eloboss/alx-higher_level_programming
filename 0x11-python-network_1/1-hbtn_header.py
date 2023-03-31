#!/usr/bin/python3
"""sends a request to the URL and displays a variable in the head"""


if __name == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        elo = response.headers.get('X-Request-Id')
        print(elo)
