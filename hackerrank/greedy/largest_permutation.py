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

def create_indexes(natural_nums):
    # Since the numbers are N natural numbers they have to be consecutive. So we know the max element from it.
    max_v = len(natural_nums)
    idx_buf = [0] * max_v
    for i, n in enumerate(natural_nums):
        idx_buf[max_v - n] = i

    return idx_buf

def largest_permutation_brute_force(K, natural_nums):
    """
    Figure out the largest permutated number that can be generated given K and a bunch of natural nums
    :param K: Number of swaps allowed
    :param natural_nums: the digits which can be swapped
    :return: The largest number
    """
    idx_buf = create_indexes(natural_nums)

    pos = 0
    swap = 0
    swap_loc = 0
    max_val = len(natural_nums)
    while swap < K and pos < len(natural_nums):
        if idx_buf[swap_loc] != pos:
            current_number = natural_nums[pos]
            to_swap_with = natural_nums[idx_buf[swap_loc]]

            swap_with_idx = idx_buf[swap_loc]

            natural_nums[idx_buf[swap_loc]], natural_nums[pos] = natural_nums[pos], natural_nums[idx_buf[swap_loc]]
            # Update the index buffer too
            idx_buf_loc = max_val - current_number
            idx_buf[idx_buf_loc] = swap_with_idx

            idx_buf[swap_loc] = pos

            swap += 1

        pos += 1
        swap_loc += 1

    str_nums = []
    for n in natural_nums:
        str_nums.append(str(n))

    return str_nums


def read(read_fn):
    N, K = [int(v) for v in read_fn().replace("\n", "").split(" ")]
    natural_nums = [int(num) for num in read_fn().strip().replace("\n", "").split(" ")]

    return K, natural_nums

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            K, natural_nums = read(f.readline)
    else:
        K, natural_nums = read(input)

    str_nums = largest_permutation_brute_force(K, natural_nums)
    print(" ".join(str_nums))

if __name__ == "__main__":
    main()