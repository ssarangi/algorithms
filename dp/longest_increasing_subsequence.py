"""
The MIT License (MIT)

Copyright (c) 2015 <Satyajit Sarangi>

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

"""
The longest Increasing Subsequence (LIS) problem is to find the length of the
longest subsequence of a given sequence such that all elements of the subsequence
are sorted in increasing order. For example, length of LIS for
{ 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15 } is 6 and LIS is {0, 2, 6, 9, 11, 15.}.
The longest increasing subsequence problem is closely related to the longest
common subsequence problem, which has a quadratic time dynamic programming solution:
the longest increasing subsequence of a sequence S is the longest common subsequence of S and T,
where T is the result of sorting S.
"""

import sys

def longest_increasing_subsequence(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    assert(0, "Not implemented yet")

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]), 6)

def main():
    print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))

if __name__ == "__main__":
    main()
    unittest.main()