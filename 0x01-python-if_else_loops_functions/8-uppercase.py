#!/usr/bin/python3

"""Start of function that prints a string in uppercase"""


def uppercase(str):
    rlt = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            upper_char = chr(ord(c) - 32)
        else:
            upper_char = c
        rlt += upper_char
    print("{}".format(rlt))
