#!/usr/bin/python3
def search_replace(my_list, search, replace):
    pen = []
    boss = len(my_list)
    for elo in range(boss):
        if my_list[elo] == search:
            pen.append(replace)
        else:
            pen.append(my_list[elo])
    return pen
