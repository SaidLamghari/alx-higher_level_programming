#!/usr/bin/python3
def magic_calculation(a, b):
    add = __import__('magic_calculation_102').add
    sub = __import__('magic_calculation_102').sub

    if a < b:
        c = add(a, b)
        i = 4
        while i <= 6:
            c = add(c, i)
            i += 1
        retun c
    else:
        return sub(a, b)
