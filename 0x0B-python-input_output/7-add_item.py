#!/usr/bin/python3
"""Write a script that adds all arguments
to a Python list, and then save them to a file:"""


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_items_to_list(filename, items):
    """
    Adds items to a Python list and saves them to a file.

    Args:
        filename (str): The name of the file to save the list to.
        items (list): The items to add to the list.

    """
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    my_list.extend(items)
    save_to_json_file(my_list, filename)
