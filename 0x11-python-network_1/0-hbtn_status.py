#!/usr/bin/python3
""" Method to fetch url """


import urllib

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as elo:
    boss = elo.read()
    print(boss)
