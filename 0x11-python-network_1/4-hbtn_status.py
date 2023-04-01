#!/usr/bin/python3
"""Script that requires the code"""


import requests

if __name == "__main__":
    elo = request.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(elo.text)))
    print('\t- content: {}'.format(elo.text))
