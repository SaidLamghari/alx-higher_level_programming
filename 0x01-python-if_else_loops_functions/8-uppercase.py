#!/usr/bin/python3

"""Start of function that prints a string in uppercase"""


def uppercase(str):
    result = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        result += uppercase_char
    print("{}".format(result))
