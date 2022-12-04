#!/usr/bin/python3
def element_at(my_list, idx):
    boss = len(my_list)
    for i in my_list:
        if idx < 0 or idx > boss - 1:
            return None
        else:
            return my_list[idx]
