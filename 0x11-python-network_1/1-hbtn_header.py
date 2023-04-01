#!/usr/bin/python3
"""
sends a request to the URL and displays a variable in the head X-Request-id
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        elo = response.headers.get('X-Request-Id')
        print(elo)
