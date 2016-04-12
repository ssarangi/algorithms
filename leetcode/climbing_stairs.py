class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        climb_types = [1, 2]
        dp = [0] * (n+1)
        
        for i in range(0, n + 1):
            if i > 2:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = i
                
        return dp[n]
    
soln = Solution()

n = 4
print(soln.climbStairs(n))