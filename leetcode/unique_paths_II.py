# https://leetcode.com/problems/unique-paths-ii/description/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])
        if num_rows == 1 and num_cols == 1:
            return int(not obstacleGrid[0][0])

        dp = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        dp[0][0] = int(not obstacleGrid[0][0])
        for col in range(1, num_cols):
            if obstacleGrid[0][col-1] == 0 and obstacleGrid[0][col] == 0:
                dp[0][col] = dp[0][col-1]
        for row in range(1, num_rows):
            if obstacleGrid[row-1][0] == 0 and obstacleGrid[row][0] == 0:
                dp[row][0] = dp[row-1][0]

        for col in range(1, num_cols):
            for row in range(1, num_rows):
                if obstacleGrid[row][col] == 1:
                    continue
                
                if obstacleGrid[row-1][col] == 0:
                    dp[row][col] = dp[row-1][col]
                if obstacleGrid[row][col-1] == 0:
                    dp[row][col] += dp[row][col-1]
        
        # Return bottom right
        return dp[-1][-1]
    
import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testMinCostClimbingStairs(self):
        self.assertEqual(self.soln.uniquePathsWithObstacles([[1]]), 0)
        self.assertEqual(self.soln.uniquePathsWithObstacles([[0]]), 1)
        self.assertEqual(self.soln.uniquePathsWithObstacles([[0,1]]), 0)
        self.assertEqual(self.soln.uniquePathsWithObstacles([[1,0]]), 0)
        self.assertEqual(self.soln.uniquePathsWithObstacles([[0],[1]]), 0)
        self.assertEqual(self.soln.uniquePathsWithObstacles([[1],[0]]), 0)
        
        self.assertEqual(self.soln.uniquePathsWithObstacles([
                                                              [0,0,0],
                                                              [0,1,0],
                                                              [0,0,0]
                                                            ]), 2)

        self.assertEqual(self.soln.uniquePathsWithObstacles([[0,1,0,0,0],
                                                             [1,0,0,0,0],
                                                             [0,0,0,0,0],
                                                             [0,0,0,0,0]]), 0)

if __name__ == "__main__":
    unittest.main()