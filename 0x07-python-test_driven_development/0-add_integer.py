#!/usr/bin/python3
"""function that adds 2 integers."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer.
        b (int or float): The second integer. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return a + b


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/0-add_integer.txt")
