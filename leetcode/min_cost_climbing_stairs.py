# https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0) # Denote the top of the floor so we don't have to add special cases
        
        cum_costs = [0] * len(cost)
        
        for idx in range(0, len(cost)):
            cum_costs[idx] = min(cum_costs[idx - 1], cum_costs[idx - 2]) + cost[idx]
        
        # Return the last element of the cumulative cost
        return cum_costs[-1]
    
import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testMinCostClimbingStairs(self):
        self.assertEqual(self.soln.minCostClimbingStairs([10, 15, 20]), 15)
        self.assertEqual(self.soln.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

if __name__ == "__main__":
    unittest.main()