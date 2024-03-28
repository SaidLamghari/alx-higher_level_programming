#!/usr/bin/python3
"""
Takes in a URL
Sends a request
Displays the body.
Handles urllib.error.HTTPError
Prints the error code.

Autor : Said LAMGHARI
"""

import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    inurl = sys.argv[1]

    rqtu = urllib.request.urlopen(inurl)

    """err_u = urllib.error.HTTPError"""

    try:
        with rqtu as response:
            """rsp = response.read().decode('utf-8')"""
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
