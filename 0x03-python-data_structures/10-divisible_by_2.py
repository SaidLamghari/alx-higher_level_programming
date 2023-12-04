#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    rlt_list = []
    for nm in my_list:
        if nm % 2 == 0:
            rlt_list.append(True)
        else:
            rlt_list.append(False)
    return rlt_list
