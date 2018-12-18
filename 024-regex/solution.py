#!/usr/bin/env python3

# Implement regular expression matching with the following special characters:
# 
#     . (period) which matches any single character
#     * (asterisk) which matches zero or more of the preceding element
# 
# That is, implement a function that takes in a string and a valid regular
# expression and returns whether or not the string matches the regular expression.
# 
# For example, given the regular expression "ra." and the string "ray", your
# function should return true. The same regular expression on the string "raymond"
# should return false.
# 
# Given the regular expression ".*at" and the string "chat", your function should
# return true. The same regular expression on the string "chats" should return
# false.

def match_regex(string, r):
    i = 0

    for char in string:
        if i >= len(r):
            return False

        c = r[i]

        if i < len(r)-1:
            if r[i+1] == '*' and (char == c or c == '.'):
                continue

        if not (c == '.' or c == char):
            return False

        i += 1

    return True

assert match_regex("ray", "ra.") == True
assert match_regex("raymond", "ra.") == False
assert match_regex("raaaaaaa", "ra*") == True
assert match_regex("chat", ".*at") == True

print("[+] All tests done.")
