# https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_cols = len(grid[0])
        num_rows = len(grid)
        if num_rows == 1 and num_cols == 1:
            return grid[0][0]

        dp = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        dp[0][0] = grid[0][0]
        
        for i in range(num_rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for i in range(num_cols):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        for col in range(1, len(grid[0])):
            for row in range(1, len(grid)):
                dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]
        
        # Return bottom right
        return dp[-1][-1]
    
import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testMinCostClimbingStairs(self):
        self.assertEqual(self.soln.minPathSum([[1,3,1],
                                               [1,5,1],
                                               [4,2,1]]), 7)

        self.assertEqual(self.soln.minPathSum([[1]]), 1)

if __name__ == "__main__":
    unittest.main()