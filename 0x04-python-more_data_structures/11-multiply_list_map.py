#!/usr/bin/python3
"""Start of function that returns a list
with all values multiplied by a number"""


def multiply_list_map(my_list=[], number=0):
    return list(map((lambda element: element * number), my_list))
