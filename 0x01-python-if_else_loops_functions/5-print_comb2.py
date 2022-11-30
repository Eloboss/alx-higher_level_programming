#!/usr/bin/python3
for e in range(00, 100):
    if e == 99:
        print(e)
    else:
        print("{:02d}".format(e), end=", ")
