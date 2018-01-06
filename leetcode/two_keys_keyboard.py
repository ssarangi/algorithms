# https://leetcode.com/problems/2-keys-keyboard/description/

import math

class Solution:
    # def find_factors(self, num):
    #     sq_num = int(math.sqrt(num))
    #     for i in range(2, sq_num+1):
    #         if num % i == 0:
    #             return num // i
        
    #     return None

    # def minSteps(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
        
    #     dp = [0] * max(4, (n + 1))
    #     dp[1] = 0
    #     dp[2] = 2
    #     dp[3] = 3
        
    #     for i in range(4, n+1):
    #         max_factor = self.find_factors(i)
            
    #         if max_factor is not None and i % 2 == 0 and i % max_factor == 0:
    #             dp[i] = min(dp[max_factor] + (i - max_factor) // max_factor + 1, dp[i//2] + 2)
    #         elif max_factor is not None and i % max_factor == 0:
    #             dp[i] = dp[max_factor] + (i - max_factor) // max_factor + 1 # One Copy of 3 elements(1) + 
    #             # all paste of 3 elements((n-3)//3 since we already have 3 elements
    #         elif i % 2 == 0:
    #             dp[i] = dp[i//2] + 2 # One Copy & One Paste
    #         else:
    #             # Prime number. So we need n steps
    #             dp[i] = i

    #     return dp[n]
    def minSteps(self, n):
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans
    
import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testMinCostClimbingStairs(self):
        self.assertEqual(self.soln.minSteps(1), 0)
        self.assertEqual(self.soln.minSteps(2), 2)
        self.assertEqual(self.soln.minSteps(3), 3)
        self.assertEqual(self.soln.minSteps(4), 4)
        self.assertEqual(self.soln.minSteps(5), 5)
        self.assertEqual(self.soln.minSteps(6), 5)
        self.assertEqual(self.soln.minSteps(7), 7)
        self.assertEqual(self.soln.minSteps(8), 6)
        self.assertEqual(self.soln.minSteps(9), 6)
        self.assertEqual(self.soln.minSteps(10), 7)
        self.assertEqual(self.soln.minSteps(11), 11)
        self.assertEqual(self.soln.minSteps(12), 7)
        self.assertEqual(self.soln.minSteps(13), 13)
        self.assertEqual(self.soln.minSteps(14), 9)
        self.assertEqual(self.soln.minSteps(15), 8)
        self.assertEqual(self.soln.minSteps(16), 8)
        self.assertEqual(self.soln.minSteps(21), 10)
        self.assertEqual(self.soln.minSteps(25), 10)
        self.assertEqual(self.soln.minSteps(189), 16) # Mine gave 19

if __name__ == "__main__":
    unittest.main()