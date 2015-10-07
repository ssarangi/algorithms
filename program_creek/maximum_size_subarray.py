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
Given an array of n positive integers and a positive integer s, find the minimal
length of a subarray of which the sum = s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7, the subarray [4,3] has the
minimal length of 2 under the problem constraint.
"""

def maximum_size_subarray(arr, target_sum):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        if arr[0] == target_sum:
            return arr
    elif len(arr) == 2:
        if arr[0] + arr[1] == target_sum:
            return arr

    ptr_left = 0
    ptr_right = 1
    sum = 0
    result = []
    while sum != target_sum and ptr_left < ptr_right:
        sum += arr[ptr_left] + arr[ptr_right]
        result.append(arr[ptr_left])
        result.append(arr[ptr_right])
        if sum < target_sum:
            ptr_right += 1
        elif sum > target_sum:
            result = []
            sum = 0
            ptr_left += 1

    return result


import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maximum_size_subarray([2,3,1,2,4,3], 7), [4,3])

def main():
    print(maximum_size_subarray([2,3,1,2,4,3], 7))

if __name__ == "__main__":
    main()
    unittest.main()