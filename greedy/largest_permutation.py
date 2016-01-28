"""
The MIT License (MIT)

Copyright (c) 2015 <Satyajit Sarangi>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

# LINK: https://www.hackerrank.com/challenges/largest-permutation

import sys

def find_largest(natural_nums):
    max_num = natural_nums[0]
    loc = 0
    for i in range(1, len(natural_nums)):
        if max_num < natural_nums[i]:
            max_num = natural_nums[i]
            loc = i

    return max_num, loc

def largest_permutation_brute_force(K, natural_nums):
    """
    Figure out the largest permutated number that can be generated given K and a bunch of natural nums
    :param K: Number of swaps allowed
    :param natural_nums: the digits which can be swapped
    :return: The largest number
    """
    for swaps in range(0, K):
        largest, loc = find_largest(natural_nums)
        # Swap the 2 numbers
        natural_nums[0], natural_nums[loc] = natural_nums[loc], natural_nums[0]

    return natural_nums


def read(read_fn):
    first_line = read_fn().split(" ")
    N = int(first_line[0])
    K = int(first_line[1])

    natural_nums = [int(num) for num in read_fn().split(" ")]

    return K, natural_nums

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            K, natural_nums = read(f.readline)
    else:
        K, natural_nums = read(input)

    output = largest_permutation_brute_force(K, natural_nums)
    print(output)

if __name__ == "__main__":
    main()