#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for elo in a_dictionary:
            if elo == key:
                a_dictionary[elo] = value
                return a_dictionary
