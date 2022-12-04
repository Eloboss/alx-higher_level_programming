#!/usr/bin/python3
def no_c(my_string):
    boss = ""
    for e in my_string:
        if e != 'c' and e != 'C':
            boss += e
    return boss
