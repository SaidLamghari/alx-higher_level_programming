#!/usr/bin/python3

""" Write a program that imports the function def add(a, b):
    from the file add_0.py and prints the result of
    the addition 1 + 2 = 3 """



if _name_ == "_main_":
    from add_0 import add
    a= 1
    b = 2
    rslt = add(a, b)
    print("{} + {}".format(a, b, rslt))
