#!/usr/bin/python3
# The function that prints x elements of a list.

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            print(i, end="")
            count += 1
            if count == x:
                break
    except TypeError:
        pass
    print()
    return count
