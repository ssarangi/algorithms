"""
The MIT License (MIT)

Copyright (c) 2015 <Satyajit Sarangi, Pranabesh Sinha>

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

# Use intermediate array
# Bubble Rotate
# Reversal

# python -m unittest rotate_array.py

import sys, logging

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

def reverse(arr, start, end):
    # if (end - start == 1):
    #     arr[start], arr[end] = arr[end], arr[start]
    #     return arr
    #
    # center = int((start + end + 1) / 2)
    # for i in range(start, center):
    #     arr[i], arr[end - i - 1] = arr[end - i - 1], arr[i]

    j = end
    for i in range(start, end):
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        j -= 1

    return arr

def rotate_arr_intermediate_array(arr, k):
    result = []
    for i in range(k + 1, len(arr)):
        result.append(arr[i])

    for i in range(0, k + 1):
        result.append(arr[i])

    return result

def bubble_rotate(arr, k):
    result = []
    # for i in range()

def inplace_rotate(arr, k):
    border = len(arr) - k - 1

    arr = reverse(arr, 0, border)
    arr = reverse(arr, border + 1, len(arr) - 1)
    arr = reverse(arr, 0, len(arr) - 1)
    return arr

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rotate_arr_intermediate_array([1,2,3,4,5,6,7], k=3), [5,6,7,1,2,3,4])
        # self.assertEqual(bubble_rotate([1,2,3,4,5,6,7], k=3), [5,6,7,1,2,3,4])
        self.assertEqual(inplace_rotate([1,2,3,4,5,6,7], k=3), [5,6,7,1,2,3,4])
        self.assertEqual(inplace_rotate([1,2,3,4,5,6,7], k=2), [6,7,1,2,3,4,5])

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    print(inplace_rotate(arr, k=2))
    # unittest.main()