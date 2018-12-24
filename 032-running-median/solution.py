#!/usr/bin/env python3

# Compute the running median of a sequence of numbers. That is, given a stream of
# numbers, print out the median of the list so far on each new element.
# 
# Recall that the median of an even-numbered list is the average of the two middle
# numbers.
# 
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# 
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

def running_median(stream):
    greater = []
    lower = []
    median = 0

    for number in stream:
        if number < median:
            lower.append(number)
        else:
            greater.append(number)

        # keep the two list balanced
        diff = len(greater) - len(lower)
        if diff > 1:
            minimum = min([x for x in greater])
            lower.append(minimum)
            greater.remove(minimum)
        elif diff < -1:
            maximum = max([x for x in lower])
            greater.append(maximum)
            lower.remove(maximum)

        # get the median
        diff = len(greater) - len(lower)
        if diff > 0:
            minimum = min([x for x in greater])
            median = minimum
        elif diff < 0:
            maximum = max([x for x in lower])
            median = maximum
        else:
            minimum = min([x for x in greater])
            maximum = max([x for x in lower])
            median = (minimum + maximum) / 2

        print(median)

seq = [2, 1, 5, 7, 2, 0, 5]
print("Running median for: {}".format(seq))
running_median(seq)
