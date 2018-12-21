#!/usr/bin/env python3

# Run-length encoding is a fast and simple method of encoding strings. The basic
# idea is to represent repeated successive characters as a single count and
# character. For example, the string "AAAABBBCCDAA" would be encoded as
# "4A3B2C1D2A".
# 
# Implement run-length encoding and decoding. You can assume the string to be
# encoded have no digits and consists solely of alphabetic characters. You can
# assume the string to be decoded is valid.

def rl_encode(string):
    encoded = ""
    last = string[0]
    counter = 1

    for c in string[1:]:
        if c == last:
            counter += 1
        else:
            encoded += str(counter) + last
            last = c
            counter = 1
    encoded += str(counter) + last

    return encoded

def rl_decode(string):
    decoded = ""

    for i in range(0, len(string), 2):
        if string[i].isdigit() and string[i+1].isalpha():
            decoded += string[i+1] * int(string[i])
        else:
            return ""

    return decoded

assert rl_encode("AAAABBBCCDAA") == "4A3B2C1D2A"
assert rl_decode( rl_encode("AAAABBBCCDAA") ) == "AAAABBBCCDAA"

print("[+] All tests done.")
