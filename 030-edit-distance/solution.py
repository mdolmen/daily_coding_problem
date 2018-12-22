#!/usr/bin/env python3

# The edit distance between two strings refers to the minimum number of character
# insertions, deletions, and substitutions required to change one string to the
# other. For example, the edit distance between “kitten” and “sitting” is three:
# substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
# 
# Given two strings, compute the edit distance between them.

# this solution is too simple and incomplete : I didn't take into account the
# possibility to do an addition in the middle of the string to make them equal,
# I considered every differences as substitions.. (ex: kitten => kiten would
# have return 3 instead of 1 : sub t->e, sub e->n del n)
def edit_distance(str1, str2):
    distance = 0
    size1 = len(str1)
    size2 = len(str2)

    diff = size1 - size2
    if diff < 0:
        diff *= -1
    distance += diff

    for i in range( min(size1, size2) ):
        if str1[i] != str2[i]:
            distance += 1

    return distance

# Solution from DCP : it fills a matrix, for which dimensions depends on the
# length of the 2 strings, with the distance of the string till some index to
# the other till anither index. That way every possible combinations are
# evaluated in O(N * M), without any redundancy in the computation.
def distance(s1, s2):
    x = len(s1) + 1 # the length of the x-coordinate
    y = len(s2) + 1 # the length of the y-coordinate

    A = [[-1 for i in range(x)] for j in range(y)]
    for i in range(x):
        A[0][i] = i

    for j in range(y):
        A[j][0] = j

    for i in range(1, y):
        for j in range(1, x):
            if s1[j- 1] == s2[i - 1]:
                A[i][j] = A[i - 1][j - 1]
            else:
                A[i][j] = min(
                        A[i - 1][j] + 1,
                        A[i][j - 1] + 1,
                        A[i - 1][j - 1] + 1
                        )
    return A[y - 1][x - 1] # return the edit distance between the two strings

assert distance("kitten", "sitting") == 3
assert distance("kitten", "sausages") == 7
assert distance("kitten", "kiten") == 1
