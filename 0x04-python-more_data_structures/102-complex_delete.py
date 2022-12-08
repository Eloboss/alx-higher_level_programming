#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    elo = list(a_dictionary.keys())
    for boss in elo:
        if value == a_dictionary.get(boss):
            del a_dictionary[boss]
    return a_dictionary
