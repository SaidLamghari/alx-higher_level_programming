#!/usr/bin/python3
"""Start of the function def magic_calculation(a, b, c) """

def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        result = a + b
        return result
    else:
        result = a * b - c
        return result
