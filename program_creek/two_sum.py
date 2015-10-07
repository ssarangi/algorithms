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
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2)
are not zero-based.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

def two_sum_naive(arr, target_sum):
    result = []

    for idx1, i in enumerate(arr):
        for idx2, j in enumerate(arr[idx1 + 1:]):
            if i + j == target_sum:
                result.append([idx1 + 1, idx1 + idx2 + 2]) # To account for the non-zero indexes

    return result

def two_sum(arr, target_sum):
    result = []
    dict = {}
    for idx, i in enumerate(arr):
        if i in dict:
            result.append([dict[i] + 1, idx + 1])
        else:
            dict[target_sum - i] = idx
    return result

# This will return only 1 result. For multiple results this algorithm won't work
def two_sum_sorted(arr, target_sum):
    result = []
    ptr_left = 0
    ptr_right = len(arr) - 1

    while ptr_left <= ptr_right:
        if arr[ptr_left] + arr[ptr_right] == target_sum:
            result.append([ptr_left + 1, ptr_right + 1])
            ptr_left += 1
        elif arr[ptr_left] + arr[ptr_right] < target_sum:
            ptr_left += 1
        elif arr[ptr_left] + arr[ptr_right] > target_sum:
            ptr_right -= 1

    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(two_sum_naive([1,2,3,4,5,6,7,8], 6), [[0,4],[1,3]])
        # self.assertEqual(two_sum(), )

def main():
    print(two_sum_naive([1,2,3,4,5,6,7,8], 6))
    print(two_sum([1,2,3,4,5,6,7,8], 6))
    print(two_sum_sorted([1,2,3,4,5,6,7,8], 6))

if __name__ == "__main__":
    main()
    # unittest.main()