#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for item in my_list[:x]:
        try:
            print(item, end=" ")
            count += 1
        except Exception as e:
            print("\nError:", e)
            break
    print("")
    return count
