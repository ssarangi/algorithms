# import sys

# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         dp = [-1] * (amount + 1)
#         dp[0] = 0
        
#         for i in range(1, amount + 1):
#             if i in coins:
#                 dp[i] = 1
#                 print(i, dp[i])
#             else:
#                 min_val = sys.maxsize
#                 for j in coins:
#                     if i > j:
#                         min_val = min(min_val, dp[i-j] + 1)
                
#                 if min_val != sys.maxsize:
#                     if min_val == 0:
#                         min_val = -1
#                     dp[i] = min_val

#         return dp[amount]
    
# soln = Solution()

# # coins = [1, 2, 5]
# # amount = 11

# # # coins = [2]
# # # amount = 3

# # # coins = [1]
# # # amount = 0

# coins = [2, 5, 10, 1]
# amount = 27

# print(soln.coinChange(coins, amount))


import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        max_coin_val = max(coins)
        dp = [-1] * (max(amount, max_coin_val)  + 1)
        dp[0] = 0

        for i in coins:
            dp[i] = 1

        for i in range(1, amount + 1):
            if i not in coins:
                min_v = sys.maxsize
                for j in coins:
                    if i > j and dp[i-j] > -1:
                        if min_v > dp[i - j]:
                            min_v = dp[i - j]

                if min_v != sys.maxsize and min_v > 0:
                    dp[i] = min_v + 1

        return dp[amount]

soln = Solution()

coins = [1, 2, 5]
amount = 11

# coins = [2]
# amount = 3

# coins = [1]
# amount = 0

# coins = [2, 5, 10, 1]
# amount = 27

# coins = [186,419,83,408]
# # coins = [419]
# amount = 838

# coins = [2]
# amount = 1

coins = [370, 417, 408, 156, 143, 434, 168, 83, 177, 280, 117]
amount = 9953

print(soln.coinChange(coins, amount))