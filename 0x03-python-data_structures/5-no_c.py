#!/usr/bin/python3
def no_c(my_string):
    boss = ""
    for i in my_string:
        if i != 'c' or i != 'C':
            boss += i
    print(boss)
