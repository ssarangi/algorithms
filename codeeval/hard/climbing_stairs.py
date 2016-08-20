import sys

def stair_climbing(total_stairs):
    dp = [0] * (total_stairs + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, total_stairs + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[total_stairs]

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        total_stairs = int(test)
        ways = stair_climbing(total_stairs)
        print(ways)