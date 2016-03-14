def does_balancing_element_exist(arr):
    # Make 2 passes. One from left and one from right
    sum_from_left = [0] * len(arr)
    sum_from_right = [0] * len(arr)

    prev_sum = 0
    for i in range(0, len(arr)):
        sum_from_left[i] = prev_sum + arr[i]
        prev_sum = sum_from_left[i]

    prev_sum = 0
    for i in range(len(arr) - 1, -1, -1):
        sum_from_right[i] = prev_sum + arr[i]
        prev_sum = sum_from_right[i]

    sum_left = 0
    sum_right = 0

    for pivot_el in range(0, len(arr)):
        if pivot_el > 0:
            sum_left = arr[pivot_el - 1]

        if pivot_el < len(arr) - 1:
            sum_right = arr[pivot_el + 1]

        if sum_left == sum_right:
            return True

    return False

import sys

def read(read_fn):
    T = int(read_fn())

    test_cases = []
    for i in range(0, T):
        N = int(read_fn())
        line = read_fn().split()
        arr = [int(i) for i in line]
        test_cases.append(arr)

    return test_cases

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            test_cases = read(f.readline)
    else:
        test_cases = read(input)

    for arr in test_cases:
        exists = does_balancing_element_exist(arr)
        if exists:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()