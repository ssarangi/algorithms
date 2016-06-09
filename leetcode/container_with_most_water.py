# https://leetcode.com/problems/container-with-most-water/

import unittest
import sys

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1 = 0
        p2 = len(height) - 1
        
        max_water = -sys.maxsize
        while p1 < p2:
            max_water = max(max_water, (p2 - p1) * min(height[p1], height[p2]))
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
                
        return max_water
    
class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testMaxArea(self):
        self.assertEqual(self.soln.maxArea([4, 1, 2, 4, 1, 4, 3]), 20)

if __name__ == "__main__":
    unittest.main()