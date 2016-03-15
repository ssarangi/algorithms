def count_luck(forest, K):
    pass

import sys

def read(read_fn):
    T = int(read_fn())

    test_cases = []
    for i in range(0, T):
        line = read_fn().split()
        N, M = int(line[0]), int(line[1])
        forest = []
        for i in range(0, N):
            s = read_fn()
            forest.append(s)

        K = int(read_fn())
        test_cases.append((forest, K))

    return test_cases


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            test_cases = read(f.readline)
    else:
        test_cases = read(input)

    for forest, K in test_cases:
        count_luck(forest, K)


if __name__ == "__main__":
    main()