#!/usr/bin/python3
def max_integer(my_list=[]):
    boss = len(my_list)
    if boss == 0:
        return None
    Max = my_list[0]
    for elo in my_list:
        if elo > Max:
            Max = elo
            return elo
    return Max
