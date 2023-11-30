#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import sub, add

    if a < b:
        c = add(a, b)
        i = 4
        while i <= 6:
            c = add(c, i)
            i += 1
        return c
    else:
        return sub(a, b)
    return 0
