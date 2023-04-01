#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to url"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv[1]) < 2:
        q = ""
    else:
        q = sys.argv[1]
    elo = http://0.0.0.0:5000/search_user
    values ={'q': q}
    boss = requests.post(elo, data=values)
    try:
        e = boss.json()
        if e == {}:
            print('No result')
        else:
            print("{[]} {}".format(e['id'], e['name']))
    except:
        print('Not a valid JSON')
