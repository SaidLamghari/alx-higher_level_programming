#!/usr/bin/python3
"""
Takes your GitHub credentials
(username and password)
Uses the GitHub API
Display your id

Autor : Said LAMGHARI
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]

    password = sys.argv[2]

    inurl = 'https://api.github.com/user'

    rqg = requests.get

    rsp = rqg(inurl, auth=(username, password))

    strsp = rsp.status_code

    if strsp != 200:
        print("None")

    if strsp == 200:
        data = rsp.json()
        print(data['id'])
