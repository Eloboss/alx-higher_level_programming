#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    total = 0
    for tup in my_list:
        sum += tup[0] * tup[1]
        total += tup[1]
    average = sum / total
    return float(average)
