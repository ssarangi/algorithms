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
There are two sorted arrays A and B of size m and n respectively. Find the
median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

def find_median(arr1, arr2):
    # since the arrays are sorted keep on recursively finding elements until all elements have been seen
    if len(arr1) > 0:
        center_1 = int(len(arr1) / 2)
        if len(arr1) % 2 == 0: center_1 -= 1
        median_1 = arr1[center_1]

    if len(arr2) > 0:
        center_2 = int(len(arr2) / 2)
        if len(arr2) % 2 == 0: center_2 -= 1
        median_2 = arr2[center_2]

    if (len(arr1)  == 0):
        return median_2

    if (len(arr2) == 0):
        return median_1

    if median_1 > median_2:
        if arr1[center_1 - 1] <= median_2:
            return median_2
        else:
            return find_median(arr1[:center_1], arr2[center_2 + 1:])
    elif median_2 > median_1:
        if arr2[center_2 - 1] <= median_1:
            return median_1
        else:
            return find_median(arr1[center_1 + 1:], arr2[:center_2])
    else:
        return median_1

def main():
    # arr1 = [1,2,3,4,5]
    # arr2 = [6,7,8,9,20,30,40,50]
    arr1 = [i for i in range(20, 40, 2)]
    arr2 = [i for i in range(1, 80, 2)]

    # arr1.extend(arr2)
    # arr1.sort()
    #
    # print(arr1)
    # print(arr1[int(len(arr1) / 2)])

    print(find_median(arr1, arr2))

import unittest

class Test(unittest.TestCase):
    def test(self):
        arr1 = [1,2,3,4,5]
        arr2 = [6,7,8,9,20,30,40,50]
        self.assertEqual(find_median(arr1, arr2), 5)

if __name__ == "__main__":
    main()