#!/usr/bin/env python3

# A builder is looking to build a row of N houses that can be of K different
# colors. He has a goal of minimizing cost while ensuring that no two neighboring
# houses are of the same color.
# 
# Given an N by K matrix where the nth row and kth column represents the cost to
# build the nth house with kth color, return the minimum cost which achieves this
# goal.

def min_cost(matrix):
    nb_houses = len(matrix[0])
    result = [0] * nb_houses

    for r, row in enumerate(matrix):
        tmp = []
        
        for c, price in enumerate(row):
            lowest = []
            for i in range(nb_houses):
                if i != c:
                    lowest.append(result[i])
            tmp.append(min(lowest) + price)
            # one line from DCP solution
            #   -> tmp.append(min(result[i] for i in range(nb_houses) if i != c) + price)

        result = tmp

    return min(result)

a = [ [12, 20, 15, 10], [13, 14, 15, 16], [1, 7, 5, 10], [18, 19, 21, 13], [25,
14, 18, 11] ]
assert min_cost(a) == 52

print("[+] All tests done.")
