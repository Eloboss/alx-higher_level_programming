#!/usr/bin/python3
def fizzbuzz():
    for e in range(1, 101):
        if (e % 3 == 0):
            print(Fizz)
        elif (e % 5 == 0):
            print(Buzz)
        elif (e % 3 == 0) and (e % 5 == 0):
            print(FizzBuzz)
        else:
            print("{:d}".format(e), end=" ")
