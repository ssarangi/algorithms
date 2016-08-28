def quicksort(arr, start, end):
    if start >= end:
        return
    
    # Select the pivot
    middle = start + (end - start) // 2
    pivot = arr[middle]
    
    i = start
    j = end
    
    while i < j:
        while arr[i] < pivot:
            i += 1
        
        while arr[j] > pivot:
            j -= 1
            
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        
    if start < j:
        quicksort(arr, start, j)
        
    if i < end:
        quicksort(arr, i, end)
    
    return arr

import unittest
import random

class UnitTest(unittest.TestCase):
    def testQuickSort(self):
        for _ in range(0, 10):
            arr = [random.randint(0, 100) for _ in range(0, 20)]
            self.assertEqual(quicksort(arr, 0, len(arr) - 1), sorted(arr))

if __name__ == "__main__":
    unittest.main()