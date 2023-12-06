#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for nm in row:
            new_row.append(nm ** 2)
        new_matrix.append(new_row)
    return new_matrix
