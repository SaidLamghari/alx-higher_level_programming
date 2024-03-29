#!/usr/bin/python3
"""
takes in a URL
Sends a request
Displays the body

Autor : Said LAMGHARI
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    rsp = requests.get(url)

    rspcode = rsp.status_code

    if rspcode < 400:
        print(rsp.text)
    if rspcode >= 400:
        print("Error code:", rspcode)
