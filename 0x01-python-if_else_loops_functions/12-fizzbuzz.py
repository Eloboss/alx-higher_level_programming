#!/usr/bin/python3
def fizzbuzz():
    for e in range(1, 101):
        if (e % 3 == 0):
            print("Fizz", end=" ")
        elif (e % 5 == 0):
            print("Buzz", end=" ")
        elif (e % 3 == 0) and (e % 5 == 0):
            print("FizzBuzz", end=" ")
        else:
            print("{:d}".format(e), end=" ")
