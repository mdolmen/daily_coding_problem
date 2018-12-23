#!/usr/bin/env python3

# Suppose you are given a table of currency exchange rates, represented as a 2D
# array. Determine whether there is a possible arbitrage: that is, whether there
# is some sequence of trades you can make, starting with some amount A of any
# currency, so that you can end up with some amount greater than A of that
# currency.
# 
# There are no transaction costs and you can trade fractional quantities.

from math import log

def arbitrage(rates):
    """
    Code is my own, and the logic from DCP's solution : I lacked graph theory
    knowledge.
    """

    # take -log() of each exchange rate to transform the problem into a
    # cumulative problem where e have to find a negative cycle
    weights = [[-log(edge) for edge in row] for row in rates]
    
    n = len(weights)

    # set all distance to infinity except the start
    distance = [float('inf')] * n
    distance[0] = 0

    # find shortest path thanks to the Bellman Ford algorithm
    for i in range(n-1):
        for src in range(n):
            for dst in range(n):
                if distance[dst] > distance[src] + weights[src][dst]:
                    distance[dst] = distance[src] + weights[src][dst]

    # detect if there is any negative cycle
    for src in range(n):
        for dst in range(n):
            if distance[dst] > distance[src] + weights[src][dst]:
                return True

#      EUR, USD, JPY, GBP
# EUR
# USD
# JPY
# GBP
rates = [[1, 1.50, 10, 0.80], [0.70, 1, 0.10, 0.70], [10, 9, 1, 13], [1.10, 1.20, 0.10, 1]]
assert arbitrage(rates)

rates = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
assert not arbitrage(rates)

print("[+] All tests done.")
