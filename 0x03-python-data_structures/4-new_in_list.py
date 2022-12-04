#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = my_list.copy()
    elo = len(i)
    if idx < 0 or idx > elo - 1:
        return i
    else:
        i[idx] = element
        return i
