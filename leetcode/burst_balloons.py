class Solution:
    def maxCoinsHelper(self, nums, total_cost):
        max_cost = total_cost
        for i in range(0, len(nums)):
            balloon = nums[i]
            left = 1 if i == 0 else nums[i-1]
            right = 1 if i == len(nums) - 1 else nums[i+1]
            new_cost = total_cost + (left * balloon * right)
            new_nums = [nums[idx] for idx in range(0, len(nums)) if idx != i]
            max_cost = max(max_cost, self.maxCoinsHelper(new_nums, new_cost))
            
        return max_cost
    
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_cost = 0
        total_cost = self.maxCoinsHelper(nums, total_cost)
        return total_cost

import unittest

class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()
    
    def testBurstBalloons(self):
        self.assertEqual(self.soln.maxCoins([3, 1, 5, 8]), 167)
        self.assertEqual(self.soln.maxCoins([35,16,83,87,84,59,48,41,20,54]), 0)
        
if __name__ == "__main__":
    unittest.main()