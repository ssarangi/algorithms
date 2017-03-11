# https://leetcode.com/problems/rotate-array/

class Solution(object):
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k < 0 or len(nums) == 1:
            return None
        
        total_reverse = k // (len(nums) - 1)
        
        for i in range(0, total_reverse):
            self.reverse(nums, 0, len(nums) - 1)
            
        
        if k % (len(nums) - 1) > 0:
            self.reverse(nums, 0, len(nums) - 1)
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k, len(nums) - 1)

        return nums

import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()
        
    def testRotate(self):
        self.assertEqual(self.soln.rotate([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])
        self.assertEqual(self.soln.rotate([1,2], 3), [2,1])
        self.assertEqual(self.soln.rotate([1,2,3,4,5,6], 11), [])
        
if __name__ == "__main__":
    unittest.main()