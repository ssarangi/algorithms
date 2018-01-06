# https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def uniquePaths(self, m, n):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if m == 1 and n == 1:
            return 1

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0
        for col in range(n):
            dp[0][col] = 1
        for row in range(m):
            dp[row][0] = 1

        for col in range(1, n):
            for row in range(1, m):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        # Return bottom right
        return dp[-1][-1]
    
import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testMinCostClimbingStairs(self):
        self.assertEqual(self.soln.uniquePaths(1, 1), 1)
        self.assertEqual(self.soln.uniquePaths(2, 1), 1)


if __name__ == "__main__":
    unittest.main()