#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for elo in sorted(a_dictionary):
        print("{}: {}".format(elo, a_dictionary[elo]))
