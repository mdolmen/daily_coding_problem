#!/usr/bin/env python3

# Given a dictionary of words and a string made up of those words (no spaces),
# return the original sentence in a list. If there is more than one possible
# reconstruction, return any of them. If there is no possible reconstruction, then
# return null.
# 
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
# string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
# 
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string
# "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath',
# 'and', 'beyond'].

# Solution from DCP
def find_sentence(s, dictionary):
    starts = {0: ''}
    for i in range(len(s) + 1):
        new_starts = starts.copy()
        for start_index, _ in starts.items():
            word = s[start_index:i]
            if word in dictionary:
                new_starts[i] = word
        starts = new_starts.copy()

    result = []
    current_length = len(s)
    if current_length not in starts:
        return None
    while current_length > 0:
        word = starts[current_length]
        current_length -= len(word)
        result.append(word)

    return list(reversed(result))

def extract_words(string, words):
    words.sort(key = lambda x: len(x))
    min_size = len(words[0])
    current_size = min_size
    sentence = []
    word = ""

    for i in range(len(string)):
        if len(word) < current_size :
            word += string[i]
        
        if len(word) == current_size:
            for w in words:
                if len(w) > len(word):
                    current_size = len(w)
                    break

                if word == w:
                    sentence.append(word)
                    word = ""
                    current_size = min_size
                    break

    return sentence

string = "thequickbrownfox"
words = ['quick', 'brown', 'the', 'fox']
print(extract_words(string, words))

string = "bedbathandbeyond"
words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
print(extract_words(string, words))
