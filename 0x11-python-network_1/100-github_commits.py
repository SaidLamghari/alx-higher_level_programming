#!/usr/bin/python3
"""
Takes in a repository name
Takes an owner name
Fetches the 10 most recent commits
Using the GitHub API,
Prints them in the format <sha>: <author name>.

Autor : Said LAMGHARI
"""

import requests
import sys

if __name__ == "__main__":
    rename = sys.argv[1]

    owname = sys.argv[2]

    inurl = f'https://api.github.com/repos/{owname}/{rename}/commits'

    rqg = requests.get

    rsp = rqg(inurl)

    comts = rsp.json()[:10]

    for comt in comts:
        idantsha = comt['sha']
        autname = comt['commit']['author']['name']
        print(f"{idantsha}: {autname}")
