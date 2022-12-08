#!/usr/bin/python3
def uniq_add(my_list=[]):
    boss = set(my_list)
    count = 0
    for elo in boss:
        count += elo
    return count
