#!/usr/bin/python3
"""
Takes in a URL
sends a request
displays the value of the X-Request-Id
found in the header.
Autor : Said LAMGHARI
"""

import urllib.request
import sys


if __name__ == "__main__":
    inurl = sys.argv[1]

    rq = urllib.request.urlopen(inurl)

    with rq as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
