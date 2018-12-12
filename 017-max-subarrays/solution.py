#!/usr/bin/env python3

# Given an array of integers and a number k, where 1 <= k <= length of the
# array, compute the maximum values of each subarray of length k.
# 
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7,
# 8, 8], since:
# 
#     10 = max(10, 5, 2)
#     7 = max(5, 2, 7)
#     8 = max(2, 7, 8)
#     8 = max(7, 8, 7)
# 
# Do this in O(n) time and O(k) space. You can modify the input array in-place and
# you do not need to store the results. You can simply print them out as you
# compute them.

def max_subarrays(array, k):
    mi = [] # indexes of maxes

    for i in range(len(array)):
        if i < k:
            while mi and array[i] > array[ mi[-1] ]:
                mi.pop()
            mi.append(i)
        else:
            print(array[ mi[0] ])

            # remove index not in any current subarray
            while mi and mi[0] <= i - k:
                mi = mi[1:]

            # remove index which value are lower than the current one
            while mi and array[i] >= array[ mi[-1] ]:
                mi.pop()

            mi.append(i)
    print(array[ mi[0] ])

# expected : 10, 7, 8, 8
array = [10, 5, 2, 7, 8, 7]
k = 3
max_subarrays(array, k)

print ("---------")
# expected : 10, 12
array = [10, 2, 5, 7, 8, 12]
k = 5
max_subarrays(array, k)
