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
Given two sorted integer arrays A and B, merge B into A as one sorted array.
"""

def merge_sorted_arrays(arr1, arr2):
    idx1 = 0
    idx2 = 0

    merged = []

    while idx1 < len(arr1) or idx2 < len(arr2):
        if idx1 >= len(arr1):
            merged.extend(arr2[idx2:])
            return merged

        if idx2 >= len(arr2):
            merged.extend(arr1[idx1:])
            return merged

        num1 = arr1[idx1]
        num2 = arr2[idx2]
        if num1 < num2:
            merged.append(num1)
            idx1 += 1
        elif num1 > num2:
            merged.append(num2)
            idx2 += 1
        else:
            merged.append(num1)
            merged.append(num2)
            idx1 += 1
            idx2 += 1

    return merged

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge_sorted_arrays([1,3,5,7,9], [2,4,6,8,10,11,12,13,14,15]), [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        self.assertEqual(merge_sorted_arrays([1,3,5,6],[1,2,3,4,5,6]), [1, 1, 2, 3, 3, 4, 5, 5, 6, 6])

def main():
    print(merge_sorted_arrays([1,3,5,7,9], [2,4,6,8,10,11,12,13,14,15]))
    print(merge_sorted_arrays([1,3,5,6],[1,2,3,4,5,6]))

if __name__ == "__main__":
    main()
    unittest.main()