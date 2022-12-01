#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

boss = len(sys.argv)
if boss != 3:
    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
a = int(sys.argv[1])
op = sys.argv[2]
b = int(sys.argv[3])
if op is "+":
    print("{} {} {} = {}".format(a, b , add(a, b)))
elif op is "-":
    print("{} {} {} = {}".format(a, b , sub(a, b)))
elif op is "*":
    print("{} {} {} = {}".format(a, b , mul(a, b)))
elif op is "/":
    print("{} {} {} = {}".format(a, b , div(a, b)))
else:
    print('Unknown operator. Available operators: +, -, * and /')
