#!/usr/bin/python3
"""
Takes in a URL
Sends a request
Displays the value of X-Request-Id

Autor: Said LAMGHARI
"""

import requests

import sys


if __name__ == "__main__":
    inurl = sys.argv[1]

    rsp = requests.get(inurl)

    hd = rsp.headers

    x_request_id = hd.get('X-Request-Id')

    print(x_request_id)
