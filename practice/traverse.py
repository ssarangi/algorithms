def count_traversals(N):
    dp = [[0 for i in range(0, N)] for j in range(0, N)]
    
    for i in range(0, N):
        dp[0][i] = 1

    for i in range(0, N):
        dp[i][0] = 1

    for x in range(1, N):
        for y in range(1, N):
            dp[y][x] = dp[y-1][x] + dp[y][x-1]

    return dp[N-1][N-1]

print(count_traversals(5))