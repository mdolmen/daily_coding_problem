#!/usr/bin/env python

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    global node_str
    if (node.val):
        node_str += node.val

    if (node.left):
        node_str += '('
        serialize(node.left)
    if (node.right):
        node_str += ')'
        serialize(node.right)

def print_tree(node):
    if (node.val):
        print(node.val)

    if (node.left):
        print_tree(node.left)
    if (node.right):
        print_tree(node.right)

# TODO : this function needs a fix
def deserialize(node_str):
    left = None
    right = None
    if '(' in node_str or ')' in node_str:
        tmp = node_str.split(')')
        print(tmp)

        if len(tmp) > 1:
            # there is something to the right
            right = deserialize(tmp[1])

        left = deserialize(tmp[0])
    else:
        n = Node(node_str)
        n.left = left
        n.right = right

    return n

node = Node('root', Node('left', Node('left.left')), Node('right'))

node_str = ""
serialize(node)
node_str += ')'
print(node_str)

new = deserialize(node_str)
print_tree(new)
