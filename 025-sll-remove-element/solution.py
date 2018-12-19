#!/usr/bin/env python3

# Given a singly linked list and an integer k, remove the kth last element from
# the list. k is guaranteed to be smaller than the length of the list.
# 
# The list is very long, so making more than one pass is prohibitively expensive.
# 
# Do this in constant space and in one pass.

class Node:
    def __init__(self, val, pnext=None):
        self.val = val
        self.pnext = pnext

    def display(self):
        n = self
        while n != None:
            print(n.val)
            n = n.pnext

def delete(head, n):
    previous = None
    current = None

    tmp = head
    count = 0

    while tmp != None:
        count += 1

        if count >= n and head != None:
            previous = current
            current = head
            head = head.pnext

        tmp = tmp.pnext

    # delete the element
    if previous != None:
        previous.pnext = current.pnext
        current = None
    else:
        # first element
        head = head.pnext

head = Node(10, (Node( 20, Node(30, Node(40)))) )

head.display()
delete(head, 2)
print("----")
head.display()
