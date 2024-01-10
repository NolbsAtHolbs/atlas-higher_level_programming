#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    maximum_value = my_list[0]
    for num in my_list:
        if num > maximum_value:
            maximum_value = num
    return maximum_value
