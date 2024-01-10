#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        iterator = iter(my_list)
        while count < x:
            print(next(iterator), end=" ")
            count += 1
    except StopIteration:
        pass
    finally:
        print("")
        return count
