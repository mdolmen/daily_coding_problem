#!/usr/bin/env python3

# Suppose we represent our file system by a string in the following manner:
# 
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
# 
# dir
#     subdir1
#     subdir2
#         file.ext
# 
# The directory dir contains an empty sub-directory subdir1 and a sub-directory
# subdir2 containing a file file.ext.
# 
# The string
# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# represents:
# 
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# 
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1
# contains a file file1.ext and an empty second-level sub-directory subsubdir1.
# subdir2 contains a second-level sub-directory subsubdir2 containing a file
# file2.ext.
# 
# We are interested in finding the longest (number of characters) absolute path to
# a file within our file system. For example, in the second example above, the
# longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is
# 32 (not including the double quotes).
# 
# Given a string representing the file system in the above format, return the
# length of the longest absolute path to a file in the abstracted file system. If
# there is no file in the system, return 0.
# 
# Note:
# 
# The name of a file contains at least a period and an extension.
# 
# The name of a directory or sub-directory will not contain a period.

def longest_path(fs):
    lengths = []
    depth = 0
    file_found = 0
    longest = 0
    nb_tab = 0
    l = 0
    i = 0

    while i < len(fs):
        nb_tab = 0

        if fs[i] == '\n':
            # +1 to for the '/'
            l += 1
            i += 1
            continue
        while fs[i] == '\t':
            nb_tab += 1
            i += 1

        if nb_tab > depth:
            # new subdir
            depth += 1
            lengths.append(l)
        elif nb_tab < depth and nb_tab > 0:
            # end of current subdir
            l = lengths.pop()
            l = lengths[len(lengths) - 1]
            depth = nb_tab
        elif nb_tab == depth and len(lengths) > 0:
            # another elements in the same subdir
            l = lengths[len(lengths) - 1]

        if fs[i] == '.':
            file_found = 1

        l += 1

        if file_found and l > longest:
            longest = l

        i += 1

    return longest

assert longest_path("dir\n\tfile.txt") == 12
assert longest_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32
print("[+] All tests done.")
