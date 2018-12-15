#!/usr/bin/env python3

# Given an array of time intervals (start, end) for classroom lectures (possibly
# overlapping), find the minimum number of rooms required.
# 
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

# Solution from DCP
def minimum_rooms(intervals):
    starts = sorted(start for start, end in intervals)
    ends = sorted(end for start, end in intervals)

    current_max = 0
    current_overlap = 0
    i, j = 0, 0
    while i < len(intervals) and j < len(intervals):
        if starts[i] < ends[j]:
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i += 1
        else:
            current_overlap -= 1
            j += 1
    return current_max

lectures = [(30, 75), (0, 50), (60, 150)]
assert minimum_rooms(lectures) == 2

lectures = [(30, 75), (0, 20), (100, 150)]
assert minimum_rooms(lectures) == 1

print("[+] All tests done.")
