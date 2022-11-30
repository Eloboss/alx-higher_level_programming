#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        z = number * -1
        return z % 10
    else:
        z = number
        return z % 10
