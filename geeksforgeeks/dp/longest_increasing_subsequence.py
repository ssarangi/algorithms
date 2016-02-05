def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n

    # Compute the LIS values in bottom up manner
    maxv = 0
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                maxv = max(maxv, lis[i])

    return maxv

def main():
    testcase1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    testcase2 = [10, 1, 2, 3, 4, 5]

    assert longest_increasing_subsequence(testcase1) == 6
    assert longest_increasing_subsequence(testcase2) == 5

if __name__ == "__main__":
    main()