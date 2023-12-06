#!/usr/bin/python3
"""Start of function that replaces all occurrences
of an element by another in a new list"""


def search_replace(my_list, search, replace):
    new = [replace if elm == search else elm for elm in my_list]
    return new
