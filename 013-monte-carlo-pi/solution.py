#!/usr/bin/env python3

# The area of a circle is defined as PI.r^2. Estimate PI to 3 decimal places using a
# Monte Carlo method.
# 
# Hint: The basic equation of a circle is x2 + y2 = r2.

import random

def estimate_pi():
    inside = 0
    total = 1000000

    for i in range(0, total):
        p = (random.uniform(-1, 1), random.uniform(-1, 1))
        if p[0]*p[0] + p[1]*p[1] < 1:
            inside += 1

    return 4 * inside / total

print("[+] Calculating PI..")
print(estimate_pi())
