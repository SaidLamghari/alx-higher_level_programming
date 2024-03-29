#!/usr/bin/python3
"""
Takes in a letter
Sends a POST request
to http://0.0.0.0:5000/search_user

Autor : Said LAMGHARI
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        qwr = ""
    if len(sys.argv) != 1:
        qwr = sys.argv[1]

    dtld = {'q': qwr}
    rsp = requests.post('http://0.0.0.0:5000/search_user', data=dtld)

    try:
        gdt = rsp.json()
        if not gdt:
            print("No result")
        if gdt:
            print(f"[{gdt['id']}] {gdt['name']}")

    except ValueError:
        print("Not a valid JSON")
