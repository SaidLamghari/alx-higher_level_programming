#!/usr/bin/env python3

"""Start of function that prints the last digit of a number"""

def print_last_digit(number):
    l_digit = abs(number) % 10
    print(l_digit)
    return l_digit
