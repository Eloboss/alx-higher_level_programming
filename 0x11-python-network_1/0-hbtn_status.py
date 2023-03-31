#!/usr/bin/python3
""" Method to fetch url """


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as elo:
    boss = elo.read()
    print('Body response:')
    print('\t- type: {}'.format(type(boss)))
    print('\t- content: {}'.format(boss))
    print('\t- utf8 content: {}'.format(boss.decode("utf-8", "replace")))
