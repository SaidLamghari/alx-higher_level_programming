#!/usr/bin/python3
"""Stat of function that adds all unique integers
in a list (only once for each integer)."""


def uniq_add(my_list):
    unique = []
    for nm in my_list:
        if nm not in unique:
            unique.append(nm)
    return sum(unique)
