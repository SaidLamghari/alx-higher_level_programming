#!/usr/bin/python3
"""
Takes in a URL
Takes an email
Sends a POST request
Displays the body

Autor : Said LAMGHARI
"""

import requests
import sys

if __name__ == "__main__":
    inurl = sys.argv[1]
    email = sys.argv[2]

    dnne = {'email': email}

    rsp = requests.post(inurl, data=dnne)

    rt = rsp.text

    print(rt)
