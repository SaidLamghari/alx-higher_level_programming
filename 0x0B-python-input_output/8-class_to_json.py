#!/usr/bin/python3
"""function that returns the dictionary description
with simple data structure (list, dictionary,
string, integer and boolean) for JSON serialization of an object:"""


def class_to_json(obj):
    """Class are serializable:
      list, dictionary, string, integer and boolean"""
    result = obj.__dict__
    return result
