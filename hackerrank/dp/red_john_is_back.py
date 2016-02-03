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

"""
https://www.hackerrank.com/challenges/red-john-is-back
"""

import math

def is_prime(num):
    if num == 0 or num == 1:
        return False

    if num == 2 or num == 3:
        return True

    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

def num_primes(num):
    primes = 0
    for i in range(0, num + 1):
        if is_prime(i):
            primes += 1

    return primes

def total_ways_to_fill(current_size):
    if current_size < 4:
        return 1
    elif current_size == 4:
        return 2
    else:
        return total_ways_to_fill(current_size - 1) + total_ways_to_fill(current_size - 4)

def red_john_is_back(N):
    """
    This is a knapsack problem
    Basically here the idea is since the height is always 4 so we can ignore that.
    So its the width. Now the width can be fit by either bricks of width 1 or 4
    :param N:
    :return:
    """
    total_ways = total_ways_to_fill(N)
    primes = num_primes(total_ways)
    return primes

import sys

def read(read_fn):
    test_cases = []
    T = int(read_fn())
    for i in range(0, T):
        N = int(read_fn())
        test_cases.append(N)

    return test_cases

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            test_cases = read(f.readline)
    else:
        test_cases = read(input)

    for N in test_cases:
        output = red_john_is_back(N)
        print(output)

if __name__ == "__main__":
    main()
