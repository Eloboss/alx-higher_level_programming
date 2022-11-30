#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        z = number * -1
    else:
        z = number
    print("{:d}".format(z % 10), end="")
    return (z % 10)
