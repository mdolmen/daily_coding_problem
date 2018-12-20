#!/usr/bin/env python3

# Given a string of round, curly, and square open and closing brackets, return
# whether the brackets are balanced (well-formed).
# 
# For example, given the string "([])[]({})", you should return true.
# 
# Given the string "([)]" or "((()", you should return false.

def is_well_formed(string):
    stack = []

    for c in string:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if c == ')' and last_open != '(' or \
                c == '}' and last_open != '{' or \
                c == ']' and last_open != '[':
                return False

    return len(stack) == 0

assert is_well_formed("([])[]({})") == True
assert is_well_formed("([(]") == False
assert is_well_formed("([[[[]]]){}") == False
assert is_well_formed(")(") == False

print("[+] All tests done.")
