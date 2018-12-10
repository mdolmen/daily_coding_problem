#!/usr/bin/env python3

# Given a stream of elements too large to store in memory, pick a random element
# from the stream with uniform probability.
#
# Reservoir sampling : https://en.wikipedia.org/wiki/Reservoir_sampling

import random

def pick_random(stream):
    subset = []
    subset_size = 10

    for i, elem in enumerate(stream):
        if i < subset_size:
            subset.append(elem)
        else:
            # Randomly replace an element in the subset
            r = random.randint(0, i)
            if r < subset_size:
                subset[r] = elem

    return subset[random.randint(0, subset_size)]

f = open("words.txt", 'r')
print(pick_random(f)[:-1])
f.close()
