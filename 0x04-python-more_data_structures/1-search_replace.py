#!/usr/bin/python3
def search_replace(my_list, search, replace):
    boss = len(my_list)
    for elo in range(boss):
        if my_list[elo] == search:
            my_list.append(replace)
            return my_list
