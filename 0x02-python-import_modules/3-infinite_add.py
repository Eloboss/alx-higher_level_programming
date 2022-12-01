#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    boss = len(sys.argv)
    for e in range(1, boss):
        sum += int(sys.argv[e])
        print("{}".format(sum))
