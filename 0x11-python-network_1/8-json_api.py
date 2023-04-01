#!/usr/bin/python3
""" script that takes in a letter and sends a POST requests to url"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    elo = "http://0.0.0.0:5000/search_user"
    values = {'q': q}
    boss = requests.post(elo, data=values)
    try:
        e = boss.json()
        if e == {}:
            print('No result')
        else:
            print("[{}] {}".format(e.get('id'), e.get('name')))
    except ValueError:
        print('Not a valid JSON')
