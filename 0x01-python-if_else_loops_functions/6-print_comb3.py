#!/usr/bin/python3
for e in range(0, 9):
    for p in range(i + 1, 10):
        if (e == 8) and (p == 9):
            print("{}{}".format(e, p))
        if (e < p):
            print("{}{}".format(e, p), end=", ")
