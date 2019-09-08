#!/usr/bin/env python3

# Given an integer n, find the next biggest integer with the same number of 1-bits
# on. For example, given the number 6 (0110 in binary), return 9 (1001).

def next_biggest_int(x):
    # isolate the least significant '1' bit
    lsb = x & -x

    # shift the next most significant bit
    next_msb = x + lsb

    # pattern to shift to the right
    right_ones = x ^ next_msb
    right_ones = int( (right_ones >> 2) / lsb )

    return next_msb | right_ones

print("Next biggest int of 6 = {}".format( next_biggest_int(6) ))
print("Next biggest int of 156 = {}".format( next_biggest_int(156) ))
print("Next biggest int of -3 = {}".format( next_biggest_int(-3) ))
