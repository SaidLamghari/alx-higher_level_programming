#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_val = my_list[0]
    for nm in my_list:
        if nm > max_val:
            max_val = nm
    return max_val
