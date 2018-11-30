#!/usr/bin/env python

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
