#!/usr/bin/env python3

# Given two singly linked lists that intersect at some point, find the
# intersecting node. The lists are non-cyclical.
# 
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the
# node with value 8.
# 
# In this example, assume nodes with the same value are the exact same node
# objects.
# 
# Do this in O(M + N) time (where M and N are the lengths of the lists) and
# constant space.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def display_node(node):
    while node != None:
        print(node.val)
        node = node.next

def find_intersection(a, b):
    while a != None and b != None:
        if a.val == b.val:
            return a
        a = a.next
        b = b.next

    return None

m0 = Node(3)
m1 = Node(7)
m2 = Node(8)
m3 = Node(10)

m0.next = m1
m1.next = m2
m2.next = m3

n0 = Node(99)
n1 = Node(1)
n2 = Node(8)
n3 = Node(10)
n4 = Node(11)
n5 = Node(3)

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

o0 = Node(1)
o1 = Node(2)

o0.next = o1

assert find_intersection(m0, n0).val == 8
assert find_intersection(m0, o0) == None
print("[+] All tests done.")
