#!/usr/bin/python3
"""Script that takes url and post data using only request package"""

import requests
import sys

if __name__ == "__main__":
    elo = requests.post(sys.argv[1]), data={'email': sys.argv[2]})
    print(elo.text)
