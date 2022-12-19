#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        int(a / b)
        sum = int(a / b)
    except ZeroError:
        sum = None
    finally:
        print("{}".format(sum))
