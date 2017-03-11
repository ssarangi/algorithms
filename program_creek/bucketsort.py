def bucketsort(arr):
    n = len(arr)
    buckets = [0] * n
    for i in range(0, n):
        buckets[i] = []
    
    for i in range(0, n):
        bi = n * arr[i]
        print(bi)
        buckets[bi].append(arr[i])
    
    for i in range(0, n):
        buckets[bi] = sorted(buckets[bi])
        
    arr = []
    for i in range(0, n):
        arr.extend(buckets[bi])
    
    return arr
    
import unittest
import random

class UnitTest(unittest.TestCase):
    def testQuickSort(self):
        for _ in range(0, 10):
            arr = [random.randint(0, 100) for _ in range(0, 20)]
            self.assertEqual(bucketsort(arr), sorted(arr))

if __name__ == "__main__":
    unittest.main()