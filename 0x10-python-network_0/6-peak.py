#!/usr/bin/python3

def find_peak(list_of_integers):
    """ Function to find highest numbers """
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
