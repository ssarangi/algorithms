"""
The MIT License (MIT)

Copyright (c) <2015> <sarangis>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

# LINK: http://www.geeksforgeeks.org/category/c-strings/

# Check if edit distance between two strings is one
# An edit between two strings is one of the following changes.
# Add a character
# Delete a character
# Change a character

def edit_distance(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    # Allocate a table
    table = [None] * (len2 + 1)

    for i in range(len2 + 1):
        table[i] = [0] * (len1 + 1)

    # Initialize the table
    for i in range(1, len2 + 1): table[i][0] = i
    for i in range(1, len1 + 1): table[0][i] = i

    # Do dynamic programming
    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if s1[j-1] == s2[i-1]:
                d = 0
            else:
                d = 1
            table[i][j] = min(table[i-1][j-1] + d,
                              table[i-1][j] + 1,
                              table[i][j-1] + 1)

    return table[len2][len1]

def main():
    str1 = "peaks"
    str2 = "geeks"
    print(edit_distance(str1, str2))

if __name__ == "__main__":
    main()