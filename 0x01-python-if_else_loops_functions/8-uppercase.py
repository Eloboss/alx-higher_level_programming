#!/usr/bin/python3
def uppercase(str):
    for e in range(len(str)):
        if ord(str[e]) >= 97 and ord(str[e]) <= 122:
            p = 32
        else:
            p = 0
        print("{:c}".format(ord(str[e]) - p), end="")
