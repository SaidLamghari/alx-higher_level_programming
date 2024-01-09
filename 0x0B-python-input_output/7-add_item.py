#!/usr/bin/python3
"""Write a script that adds all arguments
to a Python list, and then save them to a file:"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    my_list = load_from_json_file('add_item.json')
except Exception:
    my_list = []

if load_from_json_file('add_item.json'):
    my_list = load_from_json_file("add_item.json")

json_list.extend(sys.argv[1:])

save_to_json_file(my_list, 'add_item.json')
