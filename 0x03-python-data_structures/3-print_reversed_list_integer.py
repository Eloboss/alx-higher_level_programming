#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    elo = reversed(my_list)
    for bossu in elo:
        print("{:d}".format(bossu))
