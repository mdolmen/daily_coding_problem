#!/usr/bin/env python

# `cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the
# first and last element of that pair. For example, `car(cons(3, 4))` returns 3,
# and `cdr(cons(3, 4))` returns 4.
# 
# Given this implementation of cons:
# 
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# 
# Implement car and cdr.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    """ Return the first element of the pair. """
    def get_a(a, b):
        return a
    return pair(get_a)

def cdr(pair):
    """ Return the last element of the pair. """
    def get_b(a, b):
        return b
    return pair(get_b)

print("First : {}".format( car(cons(3,4))) )
print("Last : {}".format( cdr(cons(3,4))) )
