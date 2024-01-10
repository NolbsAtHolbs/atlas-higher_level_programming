#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for elementx in range(x):
            print("{:d}".format(my_list[elementx]), end=" ")
            count += 1
        print("")
    except (ValueError, TypeError, IndexError):
        pass
    return count
