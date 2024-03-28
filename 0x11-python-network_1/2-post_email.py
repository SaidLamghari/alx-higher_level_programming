#!/usr/bin/python3
"""
Takes in a URL
Takes an email
Sends a POST request
(URL with the email as paramt.)
Displays the body.

Autor: Said LAMGHARI
"""

import urllib.parse
import sys
import urllib.request


if __name__ == "__main__":
    inurl = sys.argv[1]
    email = sys.argv[2]

    vl = {'email': email}

    dnne = urllib.parse.urlencode(vl).encode('utf-8')

    rqt = urllib.request.Request(inurl, dnne=dnne)

    rqtu = urllib.request.urlopen(rqt)

    with rqtu as response:
        bd = response.read().decode('utf-8')
        print(bd)
