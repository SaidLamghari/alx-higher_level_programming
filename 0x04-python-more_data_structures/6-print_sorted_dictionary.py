#!/usr/bin/python3
"""Start of function that prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    ordered_keys = sorted(a_dictionary.keys())
    for key in ordered_keys:
        print("{}: {}".format(key, a_dictionary[key]))
