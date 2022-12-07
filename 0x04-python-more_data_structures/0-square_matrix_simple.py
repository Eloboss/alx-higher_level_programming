#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = [[e ** 2 for e in row] for row in matrix]
    return x
