#!/usr/bin/python3
def max_integer(my_list=[]):
    boss = len(my_list)
    if boss == 0:
        return None
    for i in boss:
        while i < boss:
            j = 0
            if my_list[j + i] > my_list[i + 1]:
                return my_list[j +i]
            else:
                return my_list[i + 1]

