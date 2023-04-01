#!/usr/bin/python3
"""Script that requires the code"""


if __name == "__main__":
    import requests
    
    elo = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(elo.text)))
    print('\t- content: {}'.format(elo.text))
