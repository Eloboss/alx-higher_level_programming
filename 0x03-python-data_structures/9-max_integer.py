#!/usr/bin/python3
def max_integer(my_list=[]):
    boss = len(my_list)
    if boss == 0:
        return None
    else:
        eli = my_list[0]
        for elo in range(boss):
            if my_list[i] > elo:
                elo = my_list[i]
        return elo
