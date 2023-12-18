#!/usr/bin/python3
# The function that executes a function safely.

import sys


def safe_function(fct, *args):
    try:
        rlt = fct(*args)
        return rlt
    except Exception as er:
        print("Exception: {}".format(er), file=sys.stderr)
        return None
