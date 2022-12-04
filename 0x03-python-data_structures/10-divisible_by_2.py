#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    elo = []
    for i in my_list:
        if i % 2 == 0:
            elo.append(True)
        else:
            elo.append(False)
    return elo
