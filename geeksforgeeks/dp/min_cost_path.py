"""
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost path
to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse through that cell. Total cost of a
path to reach (m, n) is sum of all the costs on that path (including both source and destination). You can only traverse
down, right and diagonally lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and
(i+1, j+1) can be traversed. You may assume that all costs are positive integers.
"""
def min_cost(matrix, m, n):
    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0 for i in range(0, cols)] for j in range(0, rows)]

    # Now we have the array reset
    dp[0][0] = matrix[0][0]

    for y in range(0, rows):
        for x in range(0, cols):
            if y == 0:
                dp[y][x] = dp[y][x-1] + matrix[y][x]

            elif x == 0:
                dp[y][x] = dp[y-1][x] + 1

            else:
                # Current path can come from 3 directions, left, diagonal top, top
                dp[y][x] = matrix[y][x] + min(dp[y-1][x],
                                              dp[y-1][x-1],
                                              dp[y][x-1])

            if y == m and x == n:
                return dp[m][n]

    return dp[m][n]

def main():
    matrix1 = [[1, 2, 3],
               [4, 8, 2],
               [1, 5, 3]]

    print(min_cost(matrix1, 2, 2))

if __name__ == "__main__":
    main()