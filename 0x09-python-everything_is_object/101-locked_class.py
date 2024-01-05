#!/usr/bin/python3
"""class LockedClass with no class or object attribut"""


class LockedClass:
    """
    A class that restricts the dynamic creation of instance attributes,
    except for the 'first_name' attribute.
    """

    __slots__ = ['first_name']
