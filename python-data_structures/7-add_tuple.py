#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    safe_tuple_a = tuple_a + (0, 0)[:max(0, 2 - len(tuple_a))]
    safe_tuple_b = tuple_b + (0, 0)[:max(0, 2 - len(tuple_b))]

    result_tuple = (safe_tuple_a[0] + safe_tuple_b[0], safe_tuple_a[1] + safe_tuple_b[1])

    return result_tuple
