#!/usr/bin/python3
"""Script that takes url and post data using only request package"""

if __name__ == "__main__":
    import requests
    import sys

    values = {'email': sys.argv[2]}
    elo = requests.post(sys.argv[1], data=values)
    print(elo.text)
