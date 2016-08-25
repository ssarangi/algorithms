# http://www.programcreek.com/2013/01/leetcode-search-insert-position/

def search_insert_position(arr, num):
    for idx in range(0, len(arr)):
        if arr[idx] >= num:
            return idx
    
    return len(arr)

import unittest

class UnitTest(unittest.TestCase):
    def testMinimumSizeSubarray(self):
        self.assertEqual(search_insert_position([1,3,5,6], 5), 2)
        self.assertEqual(search_insert_position([1,3,5,6], 2), 1)
        self.assertEqual(search_insert_position([1,3,5,6], 7), 4)
        self.assertEqual(search_insert_position([1,3,5,6], 0), 0)


if __name__ == "__main__":
    unittest.main()