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
Different sort techniques.
"""

import sys

# Bubble Sort [Best: O(n), Worst:O(N^2)]
def bubble_sort(arr):
    for i in range(0, len(arr)):
        print("Bubble Sort --> Iteration %s: %s" % (i, arr))
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# Selection Sort [Best/Worst: O(N^2)]
def selection_sort(arr):
    for i in range(0, len(arr)):
        minv = sys.maxsize
        minidx = 0
        print("Selection Sort --> Iteration %s: %s" % (i, arr))
        for j in range(i, len(arr)):
            if (minv > arr[j]):
                minv = arr[j]
                minidx = j

        arr[i], arr[minidx] = arr[minidx], arr[i]

    return arr

# Insertion Sort [Best: O(N), Worst:O(N^2)]
def insertion_sort(arr):
    for i in range(0, len(arr)):
        print("Insertion Sort --> Iteration %s: %s" % (i, arr))
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr

# Quicksort [Best: O(N lg N), Avg: O(N lg N), Worst:O(N^2)]
def quicksort(arr):
    pass

def merge_sort(arr):
    pass

# Heapsort [Best/Avg/Worst: O(N lg N)]
def heapsort(arr):
    pass

# Counting sort [Best/Avg/Worst: O(N)]
def counting_sort(arr):
    pass

# Radix sort [Best/Avg/Worst: O(N)]
def radix_sort(arr):
    pass

import unittest

class Test(unittest.TestCase):
    def test(self):
        arr = [5,1,12,-5,16]
        result = [-5,1,5,12,16]
        self.assertEqual(bubble_sort([5,1,12,-5,16]), [-5,1,5,12,16])
        self.assertEqual(selection_sort([5,1,12,-5,16]), [-5,1,5,12,16])
        self.assertEqual(insertion_sort([5,1,12,-5,16]), [-5,1,5,12,16])

def main():
    bubble_sort([5,1,12,-5,16])
    selection_sort([5,1,12,-5,16])
    insertion_sort([5,1,12,-5,16])

if __name__ == "__main__":
    main()
    unittest.main()