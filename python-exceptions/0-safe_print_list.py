#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    index = 0
    for i in range(x):
        try:
            if i < len(my_list):
                print("{:d}".format(my_list[i]), end="")
                index += 1
        except TypeError:
            print("")
            return index
        except IndexError:
            print("")
            return index
    print("")
    return index
