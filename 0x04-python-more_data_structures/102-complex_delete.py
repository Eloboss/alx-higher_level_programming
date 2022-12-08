#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    elo = list(a_dictionary.keys())
    for boss in elo:
        if a_dictionary.get(boss) == value:
            del a_dictionary[boss]
            return a_dictionary
