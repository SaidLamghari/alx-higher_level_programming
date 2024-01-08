#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to add the attribute to.
        attr (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.

    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
