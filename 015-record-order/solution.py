#!/usr/bin/env python3

# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
# 
#     record(order_id): adds the order_id to the log
#     get_last(i): gets the ith last element from the log. i is guaranteed to be
#     smaller than or equal to N.
# 
# You should be as efficient with time and space as possible.

class OrderRecord():
    def __init__(self, N):
        self.size = N
        self.buffer = []
        self.start = 0
        self.end = 0

    def record(self, order_id):
        if len(self.buffer) < self.size:
            self.buffer.append(order_id)
            self.end += 1
        else:
            self.buffer[self.start] = order_id
            self.start += 1
            self.end = (self.end + 1) % self.size

    def get_last(self, i):
        return self.buffer[(self.end - i) % self.size]

    def show(self):
        print(self.buffer)

rec = OrderRecord(5)
rec.record(1)
rec.record(2)
rec.record(3)
rec.record(4)
rec.record(5)
rec.record(6)
rec.record(7)
rec.show()
print(rec.get_last(2))
