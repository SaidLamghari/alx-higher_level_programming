#!/usr/bin/python3
"""Stat of  function that returns a new dictionary
with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    multiplied_dict = {}
    for key, value in a_dictionary.items():
        multiplied_dict[key] = value * 2
    return multiplied_dict
