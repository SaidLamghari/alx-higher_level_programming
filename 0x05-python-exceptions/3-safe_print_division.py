#!/usr/bin/python3
# The function that divides 2 integers and prints the result.

def safe_print_division(a, b):
    try:
        rlt = a / b
    except ZeroDivisionError:
        rlt = None
    finally:
        print("Inside result: {}".format(rlt))
    return rlt
