#!/usr/bin/python3

import sys

if __name__ == "__main__":
    total_sum = sum(int(arg) for arg in sys.argv[1:])
    print(total_sum)
