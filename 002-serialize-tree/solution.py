#!/usr/bin/env python

# Given the root to a binary tree, implement serialize(root), which serializes the
# tree into a string, and deserialize(s), which deserializes the string back into
# the tree.
# 
# For example, given the following Node class
# 
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# The following test should pass:
# 
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(node):
    """
    Utility function to print a binary tree.
    """
    if (node.val):
        print(node.val)

    if (node.left):
        print_tree(node.left)
    if (node.right):
        print_tree(node.right)

def serialize(node):
    """
    Serialize a binary tree and return a string.
    """
    node_str = ""

    if (node.val):
        node_str += node.val

    if (node.left):
        node_str += '('
        node_str += 'L' + serialize(node.left)
    if (node.right):
        node_str += ')'
        node_str += 'R' + serialize(node.right)

    return node_str

def deserialize(node_str):
    """
    Deserialize a string into a binary tree (a Node object).
    """
    n = None
    left = None
    right = None
    tmp = ""

    # Parse the root.
    if '(' in node_str:
        tmp = node_str.split('(')[0]
        n = Node(tmp)
        tmp = node_str[len(tmp)+1:]
    elif ')' in node_str:
        tmp = node_str.split(')')[0]
        n = Node(tmp)
        tmp = node_str[len(tmp)+1:]
    else:
        # This node has no subtrees. 
        n = Node(node_str)

    # Parse the subtree.
    split_index = tmp.rfind(')')

    if tmp and split_index != -1:
        # A close bracket signals the end of a subtree.
        branches = [ tmp[:split_index], tmp[split_index+1:] ]

        if (branches[0][0] == 'L'):
            n.left = deserialize(branches[0][1:])
        else:
            n.right = deserialize(branches[0][1:])

        if len(branches) > 1 and len(branches[1]) > 0:
            # This subtree has 2 branches.
            if (branches[1][0] == 'L'):
                n.left = deserialize(branches[1][1:])
            else:
                n.right = deserialize(branches[1][1:])
    elif tmp:
        # 'tmp' contains only a node value.
        if (tmp[0] == 'L'):
            n.left = deserialize(tmp[1:])
        else:
            n.right = deserialize(tmp[1:])

    return n

node = Node('root', Node('left', Node('left.left')), Node('right'))
if deserialize(serialize(node)).left.left.val == 'left.left':
    print("[+] Test 1 OK.")

node2 = Node('root', None, Node('right'))
if deserialize(serialize(node2)).right.val == 'right':
    print("[+] Test 2 OK.")

node3 = Node('root', Node('left', Node('left.left')))
if deserialize(serialize(node3)).left.left.val == 'left.left':
    print("[+] Test 3 OK.")
