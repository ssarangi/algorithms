def lcs_recursive(arr1, arr2, m, n):
    if m == 0 or n == 0:
        return 0
    elif arr1[m-1] == arr2[n-1]:
        return 1 + lcs_recursive(arr1, arr2, m-1, n-1)
    else:
        return max(lcs_recursive(arr1, arr2, m, n-1), lcs_recursive(arr1, arr2, m-1, n))

def lcs_dp(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    lcs = [[0 for i in range(0, m + 1)] for j in range(0, n + 1)]

    for y in range(1, n+1):
        for x in range(1, m+1):
            if arr1[x-1] == arr2[y-1]:
                lcs[y][x] = 1 + lcs[y-1][x-1]

            else:
                lcs[y][x] = max(lcs[y-1][x], lcs[y][x-1])

    return lcs[-1][-1]

def main():
    testcase1_1 = "ABCDGH"
    testcase1_2 = "AEDFHR"

    s1 = "AGGTAB"
    s2 = "G"

    print(lcs_dp(s1, s2))
    print(lcs_dp(testcase1_1, testcase1_2))
    assert lcs_recursive(testcase1_1, testcase1_2, len(testcase1_1), len(testcase1_2)) == 3

if __name__ == "__main__":
    main()