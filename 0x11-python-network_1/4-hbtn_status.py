#!/usr/bin/python3
"""
using requests to Fetches https://alx-intranet.hbtn.io/status
Displays the body

Autor : Said LAMGHARI
"""

import requests


if __name__ == "__main__":
    inurl = 'https://alx-intranet.hbtn.io/status'

    rsp = requests.get(inurl)

    bd = rsp.text

    print("Body response:")
    print("\t- type:", type(bd))
    print("\t- content:", bd)
