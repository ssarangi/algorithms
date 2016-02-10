def insert(s, c):
    s = c + s
    return s

def remove(s):
    s = s[1:]
    return s

def replace(s, c):
    s = c + s[1:]
    return s

def edit_distance_recursive(s1, s2):
    if s1 == "" or s2 == "":
        return 0

    if s1[0] == s2[0]:
        return edit_distance_recursive(s1[1:], s2[1:])

    max_distance = min(1 + edit_distance_recursive(insert(s1, s2[0]), s2),
                       1 + edit_distance_recursive(remove(s1), s2),
                       1 + edit_distance_recursive(replace(s1, s2[0]), s2))

    return max_distance


# Transform s1 into s2
def edit_distance_dp(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for i in range(0, n + 1)] for j in range(0, m + 1)]

    for i in range(m+1):
        for j in range(n+1):
            c1 = s1[i-1]
            c2 = s2[j-1]

            # If s1 is empty, then we have to insert all characters of s2 into s1
            if i == 0:
                dp[i][j] = j
            # If s2 is empty, then we have to remove all the characters of s1
            elif j == 0:
                dp[i][j] = i

            # If the current characters matched, then the cost is the same
            elif (c1 == c2):
                dp[i][j] = dp[i-1][j-1]
            else:
                # Now consider the cost of insertion, removal
                dp[i][j] = 1 + min(dp[i][j-1], # Insert
                                   dp[i-1][j], # Delete
                                   dp[i-1][j-1]) # Replace

    return dp[m][n]


def main():
    t1 = ["geek", "gesek"]
    ed = edit_distance_recursive(t1[0], t1[1])
    print(ed)
    ed = edit_distance_dp(t1[0], t1[1])
    print(ed)

if __name__ == "__main__":
    main()