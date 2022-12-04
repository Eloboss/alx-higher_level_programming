#!/usr/bin/python3
def no_c(my_string):
    boss = ""
    for e in my_string:
        if e != 'c' or e != 'C':
            boss += e
    print(boss)
