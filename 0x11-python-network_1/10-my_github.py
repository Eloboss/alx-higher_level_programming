#!/usr/bin/python3
"""Script that takes your GitHub credentials username and password"""


import requests
import sys

if __name__ == "__main__":
    elo = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    boss = requests.get('https://api.github.com/user', auth=elo)
    try:
        e = boss.json()
        print(e['id'])
    except:
        print('None')
