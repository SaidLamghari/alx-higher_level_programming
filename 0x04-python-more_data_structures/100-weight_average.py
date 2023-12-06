#!/usr/bin/python3
"""Start of function that returns the weighted average"""


def weight_average(my_list=[]):
    if my_list:
        sm_pt = 0
        sm_wts = 0

        for score, weight in my_list:
            sm_pt += score * weight
            sm_wts += weight

        wd_average = sm_pt / sm_wts
        return wd_average
    else:
        return 0
