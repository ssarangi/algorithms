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
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the
sorted order, not the kth distinct element.

For example, given [3,2,1,5,6,4] and k = 2, return 5.

Note: You may assume k is always valid, 1 ≤ k ≤ array's length.

Soln: This can be sorted and then you find the kth largest. O(nlogn)
"""

import sys

def kth_largest(arr, k):
    top_k = [-sys.maxsize] * k
    for i in arr[1:]:
        for idx in range(0, len(top_k)):
            if i > top_k[idx]:
                top_k.insert(idx, i)
                top_k.pop()
                break

    return top_k[-1]

def main():
    arr = [3,2,1,5,6,4]
    k = 2
    print(kth_largest(arr, k))

import unittest

class Test(unittest.TestCase):
    def test(self):
        arr = [3,2,1,5,6,4]
        k = 2
        self.assertEqual(kth_largest(arr, k), 5)

if __name__ == "__main__":
    main()