#!/usr/bin/python3
"""function that returns the list of available
attributes and methods of an object"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the available
        attributes and methods of the object.

    """
    return dir(obj)
