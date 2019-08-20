#!/usr/bin/env python3

def reduce(lst, fct, init_value):
    result = init_value

    for i in lst:
        result = fct(result, i)

    return result

def add(a, b):
    return a + b

def sum(lst):
    return reduce(lst, add, 0)

numbers = [1, 2, 3, 4]
print(sum(numbers))
