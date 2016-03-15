def maximize_sum(arr, M):
    max_sum = -sys.maxsize
    for i in range(0, len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            max_sum = max(max_sum, sum % M)

    return max_sum

import sys

def read(read_fn):
    T = int(read_fn())

    test_cases = []
    for i in range(0, T):
        line = read_fn().split()
        N, M = int(line[0]), int(line[1])
        line = read_fn().split()
        arr = [int(i) for i in line]
        test_cases.append((M, arr))

    return test_cases

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            test_cases = read(f.readline)
    else:
        test_cases = read(input)

    for M, arr in test_cases:
        max_sum = maximize_sum(arr, M)
        print(max_sum)


if __name__ == "__main__":
    main()