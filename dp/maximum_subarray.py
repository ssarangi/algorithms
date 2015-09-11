__author__ = 'sarangis'

'''
Problem Statement

Given an array A={a1,a2,...,aN} of N elements, find the maximum possible sum of a

Contiguous subarray
Non-contiguous (not necessarily contiguous) subarray.
Empty subarrays/subsequences should not be considered.

This Youtube video by Ben Wright might be useful to understand the Kadane algorithm for the maximum subarray in a 1-D sequence.

Input Format

First line of the input has an integer T. T cases follow.
Each test case begins with an integer N. In the next line, N integers follow representing the elements of array A.

Constraints:

1?T?10
1?N?105
?104?ai?104
The subarray and subsequences you consider should have at least one element.

Output Format

Two, space separated, integers denoting the maximum contiguous and non-contiguous subarray. At least one integer should be selected and put into the subarrays (this may be required in cases where all elements are negative).

Sample Input

2
4
1 2 3 4
6
2 -1 2 3 4 -5
Sample Output

10 10
10 11
Explanation

In the first case:
The max sum for both contiguous and non-contiguous elements is the sum of ALL the elements (as they are all positive).

In the second case:
[2 -1 2 3 4] --> This forms the contiguous sub-array with the maximum sum.
For the max sum of a not-necessarily-contiguous group of elements, simply add all the positive elements.
'''

def maximum_contiguous_subarray(L):
    current_sum = 0
    current_index = -1
    best_sum = 0
    best_start_index = -1
    best_end_index = -1

    for i in range(len(L)):
        val = current_sum + L[i]
        if val > 0:
            if current_sum == 0:
                current_index = i
            current_sum = val
        else:
            current_sum = 0

        if current_sum > best_sum:
            best_sum = current_sum
            best_start_index = current_index
            best_end_index = i

    return L[best_start_index: best_end_index + 1]

def maximum_noncontiguous_subarray(L):
    best_list = []

    current_sum = 0
    for i in L:
        current_sum += i
        if current_sum > current_sum - i:
            best_list.append(i)

    return best_list

def main():
    test_cases = int(input())

    for i in range(0, test_cases):
        N = int(input())
        arr = [int(num) for num in (input().split(' '))]
        contiguous = maximum_contiguous_subarray(arr)
        non_contiguous = maximum_noncontiguous_subarray(arr)
        s1 = sum(contiguous)
        s2 = sum(non_contiguous)
        print("%s %s" % (s1, s2))

if __name__ == "__main__":
    main()
