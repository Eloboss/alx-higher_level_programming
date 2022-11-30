#!/usr/bin/python3
def uppercase(str):
    for e in range(len(str)):
        if ord(str[e]) >= 97 and ord(str[e]) < = 122:
            print("{:c}".format(ord(str[e]) - 32), end="")
        else:
            print("{:c}".format(ord(str[e]), end="")
