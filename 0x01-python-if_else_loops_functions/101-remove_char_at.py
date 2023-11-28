#!/usr/bin/python3

"""Start of  function that creates a copy of the string,
    removing the character at the position n
    (not the Python way, the “C array index”) """


def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    return new_str
