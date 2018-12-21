#!/usr/bin/env python3

# Write an algorithm to justify text. Given a sequence of words and an integer
# line length k, return a list of strings which represents each line, fully
# justified.
# 
# More specifically, you should have as many words as possible in each line. There
# should be at least one space between each word. Pad extra spaces when necessary
# so that each line has exactly length k. Spaces should be distributed as equally
# as possible, with the extra spaces, if any, distributed starting from the left.
# 
# If you can only fit one word on a line, then you should pad the right-hand side
# with spaces.
# 
# Each word is guaranteed not to be longer than k.
# 
# For example, given the list of words ["the", "quick", "brown", "fox", "jumps",
# "over", "the", "lazy", "dog"] and k = 16, you should return the following:
# 
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

def justify(words, k):
    lines = []
    line = ""
    length = 0
    subset = []
    i = 0

    while i < len(words):
        while length + len(words[i]) + len(subset) <= k:
            subset.append(words[i])
            length += len(words[i])
            i += 1
            if i >= len(words):
                break

        nb_spaces = k - length
        nb_words = len(subset)-1

        if nb_words == 1:
            line = subset[0] + ' '*nb_spaces
        else:
            distributed = nb_spaces // nb_words
            extra = nb_spaces % nb_words

            for word in subset[:-1]:
                line += word + ' '*distributed
                if extra > 0:
                    line += ' '
                    extra -= 1
            line += subset[-1]

        lines.append(line)
        line = ""
        length = 0
        subset = []

    return lines

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16
print( justify(words, k) )
