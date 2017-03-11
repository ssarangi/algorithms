# https://leetcode.com/problems/trapping-rain-water/

import unittest
import sys

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pass


class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testMaxArea(self):
        self.assertEqual(self.soln.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)

if __name__ == "__main__":
    unittest.main()