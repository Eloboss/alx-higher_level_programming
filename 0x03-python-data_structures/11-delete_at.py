#!/usr\bin/python3
def delete_at(my_list=[], idx=0):
    boss = len(my_list)
    elo = del my_list[idx]
    if idx < 0 or idx > boss - 1:
        return my_list
    else:
        return elo
