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
https://www.hackerrank.com/challenges/unbounded-knapsack
"""

def all_multiples(el, k):
    arr = []
    counter = 1
    while True:
        res = el * counter
        if res <= k:
            arr.append(res)
        else:
            break

        counter += 1

    return arr

def knapsack(k, els):
    # Create all possible ways in which we can select the same element multiple times
    prevarr = []
    max_sum = 0
    for el in els:
        if el > k:
            continue
        elif el == k:
            return k

        multiples_arr = all_multiples(el, k)

        max_multiples = 0
        if len(multiples_arr) > 0:
            max_multiples = multiples_arr[-1]

        max_sum = max(max_sum, max_multiples)
        # Find the last element and check if we already found the sum
        if max_multiples == k:
            return k

        newarr = [el for el in prevarr] + [el for el in multiples_arr]
        if len(prevarr) > 0:
            for multiple in multiples_arr:
                for p in prevarr:
                    sum = p + multiple

                    if max_sum == k:
                        return k

                    if p + multiple <= k:
                        newarr.append(p + multiple)
                        max_sum = max(sum, max_sum)

        prevarr = newarr

    return max_sum

import sys

def read(read_fn):
    test_cases = []
    T = int(read_fn())
    for i in range(0, T):
        N, k = [int(v) for v in read_fn().replace("\n", "").split(" ")]
        els = [int(price) for price in read_fn().replace("\n", "").split(" ")]
        test_cases.append((k, els))

    return test_cases

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            test_cases = read(f.readline)
    else:
        test_cases = read(input)

    for k, els in test_cases:
        max_sum = knapsack(k, els)
        print(max_sum)

if __name__ == "__main__":
    main()