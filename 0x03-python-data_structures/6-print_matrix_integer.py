#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rw in matrix:
        for idx in range(len(rw)):
            print("{:d}".format(rw[idx]), end="")
            if idx != len(rw) - 1:
                print(" ", end="")
        print()
