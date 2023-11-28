#!/usr/bin/python3


""" Start of function that checks for lowercase character """


def islower(a):
    if ord(a) >= 97 and ord(a) <= 122:
        return True
    else:
        return False
