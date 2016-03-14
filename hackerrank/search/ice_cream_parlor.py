def two_elements_sum(arr, M):
    dict = {}
    for i, ci in enumerate(arr):
        dict[ci] = i

    for i, ci in enumerate(arr):
        other = M - ci
        if other in dict and dict[other] != i:
            return min(i, dict[other]), max(i, dict[other])

    return -1, -1

import sys

def read(read_fn):
    T = int(read_fn())

    test_cases = []
    for i in range(0, T):
        M = int(read_fn())
        N = int(read_fn())
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

    for M, cost in test_cases:
        i1, i2 = two_elements_sum(cost, M)
        print(i1 + 1, i2 + 1)


if __name__ == "__main__":
    main()