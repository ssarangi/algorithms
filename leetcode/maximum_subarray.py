# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_val = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            max_val = max(max_val, dp[i])

        return max_val
    
import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testMinCostClimbingStairs(self):
        self.assertEqual(self.soln.maxSubArray([1]), 1)
        self.assertEqual(self.soln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)


if __name__ == "__main__":
    unittest.main()