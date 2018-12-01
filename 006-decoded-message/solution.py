#!/usr/bin/env python

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.
# 
# For example, the message '111' would give 3, since it could be decoded as 'aaa',
# 'ka', and 'ak'.
# 
# You can assume that the messages are decodable. For example, '001' is not
# allowed.
#
# Got help from : https://www.youtube.com/watch?v=qli-JCrSwuk
# Note for myself : I had the wrong approach, I started with a longer message (5
# or 6) and get lost with the combination of possibilities. A better approach is
# to start with the smallest possible message and start from there to build
# solution.

#import string
#
#letters = list(string.ascii_lowercase)
#msg = "107"
#
#one = []
#two = []
#
## list possible characters into 2 lists : one for the letters composed of one
## digit and the other for the letters composed of 2
#for i in range(len(msg)):
#    c1 = letters[ int(msg[i])-1 ]
#    print(c1)
#    if (c1 > 0):
#        one.append(c1)
#    
#    if i < len(msg)-1:
#        c2 = int(msg[i:i+2])-1
#        if (c2 < 26):
#            two.append(letters[c2])
#
#print(one)
#print(two)

def num_ways(msg):
    if len(msg) == 0:
        return 1

    if msg[0] == '0':
        return 0

    result = num_ways(msg[1:])

    if len(msg) >= 2 and int(msg[:2]) < 26:
        result += num_ways(msg[2:])

    return result

assert num_ways("112") == 3
assert num_ways("11211234") == 21
assert num_ways("10102") == 1
print("[+] All tests done.")
