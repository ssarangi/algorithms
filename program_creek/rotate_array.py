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

def rotate_arr_intermediate_array(arr, k):
    result = []
    for i in range(k + 1, len(arr)):
        result.append(arr[i])

    for i in range(0, k + 1):
        result.append(arr[i])

    return result

def bubble_rotate(arr, k):
    result = []
    for i in range()

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rotate_arr_intermediate_array([1,2,3,4,5,6,7], k=3), [5,6,7,1,2,3,4])
        self.assertEqual(bubble_rotate([1,2,3,4,5,6,7], k=3), [5,6,7,1,2,3,4])

if __name__ == "__main__":
    unittest.main()