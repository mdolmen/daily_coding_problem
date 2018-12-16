#!/usr/bin/env python3

# You are given an M by N matrix consisting of booleans that represents a board.
# Each True boolean represents a wall. Each False boolean represents a tile you
# can walk on.
# 
# Given this matrix, a start coordinate, and an end coordinate, return the minimum
# number of steps required to reach the end coordinate from the start. If there is
# no possible path, then return null. You can move up, left, down, and right. You
# cannot move through walls. You cannot wrap around the edges of the board.
# 
# For example, given the following board:
# 
# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# 
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number
# of steps required to reach the end is 7, since we would need to go through (1,
# 2) because there is a wall everywhere else on the second row.

from collections import deque

def allowed(board, row, col):
    if row < 0 or row >= len(board):
        return False
    if col < 0 or col >= len(board[0]):
        return False
    # board[x][y] == T if there is a wall
    return not board[row][col]

def get_neighbours(board, row, col):
    return [(r, c) for r, c in [
        (row, col - 1),
        (row, col + 1),
        (row - 1, col),
        (row + 1, col)] if allowed(board, r, c) ]

def shortest_path(board, start, end):
    steps = 0
    seen = [start]

    # coordinates + nb steps to get there
    queue = deque( [(start , 0)] )

    while queue:
        coord, steps = queue.popleft()
        if coord == end:
            break

        seen.append(coord)
        for n in get_neighbours(board, coord[0], coord[1]):
            if n not in seen:
                queue.append((n, steps + 1))

    return steps

board = [[False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]]
start = (3, 0)
end = (0, 0)
assert shortest_path(board, start, end) == 7

board = [[False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]]
start = (2, 1)
end = (0, 0)
assert shortest_path(board, start, end) == 3

print("[+] All tests done.")
