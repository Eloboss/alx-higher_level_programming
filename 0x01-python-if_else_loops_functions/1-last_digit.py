#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    z = (number * -1)
else:
    z = number:
if z > 5:
    print(f"Last digit of {number} is {z} and is greater than 5")
elif z == 0:
    print(f"Last digit of {number} is {z} and is 0")
else:
    print(f"Last digit of {number} is {z} and not 0")
