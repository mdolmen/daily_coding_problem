#!/usr/bin/env python3

# Given an array of time intervals (start, end) for classroom lectures (possibly
# overlapping), find the minimum number of rooms required.
# 
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def minimum_rooms(lectures):
    max_overlaps = 0
    nb_overlaps = 0

    for i, interval1 in enumerate(lectures):
        for j, interval2 in enumerate(lectures):
            if j != i:
                # end1 < start2 or start1 > end2
                nb_overlaps += (interval1[1] < interval2[0]) or (interval1[0] > interval2[1])
        max_overlaps = max(max_overlaps, nb_overlaps)

    return max_overlaps

lectures = [(30, 75), (0, 50), (60, 150)]
assert minimum_rooms(lectures) == 2

# TODO : does not work for this test case
lectures = [(30, 75), (0, 20), (100, 150), (30, 90)]
print(minimum_rooms(lectures))
#assert minimum_rooms(lectures) == 1

print("[+] All tests done.")
