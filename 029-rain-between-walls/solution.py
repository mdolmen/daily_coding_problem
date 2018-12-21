#!/usr/bin/env python3

# You are given an array of non-negative integers that represents a
# two-dimensional elevation map where each element is unit-width wall and the
# integer is the height. Suppose it will rain and all spots between two walls get
# filled up.
# 
# Compute how many units of water remain trapped on the map in O(N) time and O(1)
# space.
# 
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the
# middle.
# 
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in
# the second, and 3 in the fourth index (we cannot hold 5 since it would run off
# to the left), so we can trap 8 units of water.

def count_water_units(walls):
    units = 0

    for i in range(1, len(walls)):
        w1 = walls[i-1]
        w2 = walls[i]
        diff = w1 - w2

        if diff > 0:
            units += diff
            walls[i] += diff

    return units

walls = [2, 1, 2]
assert count_water_units(walls) == 1

walls = [3, 0, 1, 3, 0, 5]
assert count_water_units(walls) == 8

walls = [10, 3, 15, 2, 4, 9]
assert count_water_units(walls) == 37

print("[+] All tests done.")
