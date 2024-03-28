#!/usr/bin/python3
"""
Using urllib to fetches https://alx-intranet.hbtn.io/status
disp. the body of response.
Autor : Said LAMGHARI
"""

import urllib.request


if __name__ == "__main__":
    inurl = 'https://alx-intranet.hbtn.io/status'

    rq = urllib.request.urlopen(inurl)

    with rq as response:
        bd = response.read()
        print("Body response:")
        print("\t- type:", type(bd))
        print("\t- content:", bd)
        print("\t- utf8 content:", bd.decode('utf-8'))
