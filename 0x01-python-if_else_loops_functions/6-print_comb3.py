#!/usr/bin/python3
for e in range(0, 9):
    for p in range(0, 9):
        if e < p:
            print("{}{}".format(e, p), end=", ")
