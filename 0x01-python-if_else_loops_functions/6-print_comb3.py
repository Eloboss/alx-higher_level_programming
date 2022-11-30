#!/usr/bin/python3
for e in range(0, 10):
    for p in range(0, 10):
        if e < p:
            print("{}{}".format(e, p), end=", ")
            if (e == 8):
                print("{}{}".format(e, p))
