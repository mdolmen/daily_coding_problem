#!/usr/bin/env python3

# Implement locking in a binary tree. A binary tree node can be locked or unlocked
# only if all of its descendants or ancestors are not locked.
# 
# Design a binary tree node class with the following methods:
# 
#     is_locked, which returns whether the node is locked
#     
#     lock, which attempts to lock the node. If it cannot be locked, then it
#     should return false. Otherwise, it should lock it and return true.
#     
#     unlock, which unlocks the node. If it cannot be unlocked, then it should
#     return false. Otherwise, it should unlock it and return true.
# 
# You may augment the node to add parent pointers or any other property you would
# like. You may assume the class is used in a single-threaded program, so there is
# no need for actual locks or mutexes. Each method should run in O(h), where h is
# the height of the tree.

class Node:
    def __init__(self, val, ancestor=None):
        self.ancestor = ancestor
        self.val = val
        self.locked = 0
        self.descendants_locked = 0

    def is_locked(self):
        return self.locked

    def lock(self):
        if self.locked or self.descendants_locked > 0:
            return False

        # Is there a parent locked
        n = self.ancestor
        while n != None:
            if n.locked:
                return False
            n = n.ancestor

        self.locked = 1

        # Increment nb descendants locked
        m = self.ancestor
        while m != None:
            m.descendants_locked += 1
            m = m.ancestor

    def unlock(self):
        if not self.locked:
            return False
        
        self.locked = 0

        n = self.ancestor
        while n != None:
            n.descendants_locked -= 1
            n = n.ancestor

n0 = Node(0)
n1 = Node(1, n0)
n2 = Node(1, n0)
n3 = Node(1, n1)
n4 = Node(0, n1)
n5 = Node(1, n2)
n6 = Node(1, n2)

assert n3.is_locked() == 0

n3.lock()
assert n3.is_locked() == 1
assert n0.lock() == 0

n3.unlock()
assert n3.is_locked() == 0

print("[+] All tests done.")
