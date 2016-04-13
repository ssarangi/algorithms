import sys

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        max_sq_v = 1

        for i in range(2, n + 1):
            minv = sys.maxsize
            for j in range(max_sq_v + 1, 0, -1):
                square_v = j * j

                if square_v <= i:
                    if minv > dp[i-square_v]:
                        minv = dp[i-square_v] + 1

                    if j > max_sq_v:
                        max_sq_v = j

            if minv != sys.maxsize:
                dp[i] = minv

        return dp[n]

soln = Solution()
n = 6255
print(soln.numSquares(n))