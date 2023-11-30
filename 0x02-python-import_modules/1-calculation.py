#!/usr/bin/python3

""" Start of program that imports functions
    from the file calculator_1.py """


if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    a = 10
    b = 5
    r_add = add(a, b)
    r_sub = sub(a, b)
    r_mul = mul(a, b)
    r_div = div(a, b)
    print("{} + {} = {}".format(a, b, r_add))
    print("{} + {} = {}".format(a, b, r_sub))
    print("{} + {} = {}".format(a, b, r_mul))
    print("{} + {} = {}".format(a, b, r_div))
