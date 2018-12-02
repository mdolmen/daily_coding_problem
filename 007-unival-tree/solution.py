#!/usr/bin/env python

# A unival tree (which stands for "universal value") is a tree where all nodes
# under it have the same value.
# 
# Given the root to a binary tree, count the number of unival subtrees.
# 
# For example, the following tree has 5 unival subtrees:
# 
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def unival_tree(tree):
    result = 0

    if (tree.val):
        if tree.left and tree.right:
            result += (tree.left.val == tree.right.val)
        elif tree.left == None and tree.right == None:
            result += 1

    if (tree.left):
        result += unival_tree(tree.left)
    if (tree.right):
        result += unival_tree(tree.right)

    return result

node = Node( '0', Node('1'), Node('0', Node('1', Node('1'), Node('1')), Node('0')) )
assert unival_tree(node) == 5
node = Node('0')
assert unival_tree(node) == 1

print("[+] All tests done.")
