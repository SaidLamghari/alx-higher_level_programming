#!/usr/bin/python3
"""Start of function that computes the square
value of all integers of a matrix using map"""


def square_matrix_map(matrix=[]):
    return list(map(lambda r: list(map(lambda x: x * x, r)), matrix))
