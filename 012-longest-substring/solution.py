#!/usr/bin/env python

# Given an integer k and a string s, find the length of the longest substring
# that contains at most k distinct characters.
# 
# For example, given s = "abcba" and k = 2, the longest substring with k distinct
# characters is "bcb".

def longest_substr(s, k):
    chars_met = 0
    chars = [0] * 26
    substr = ""
    tmp = ""

    for i in range(0, len(s)):
        index = ord(s[i]) - ord('a')

        if chars_met < k:
            substr += s[i]

            if chars[index] == 0:
                chars[index] = 1
                chars_met += 1
        elif chars_met == k and chars[index] == 1:
            substr += s[i]
        else:
            break
    if len(s[1:]) > len(substr):
        tmp = longest_substr(s[1:], k)
    
    return substr if len(substr) > len(tmp) else tmp

assert longest_substr("abcba", 2) == "bcb"
assert longest_substr("abcdeff", 2) == "eff"
assert longest_substr("abcdffjtheef", 5) == "ffjtheef"

print("[+] All tests done.")
