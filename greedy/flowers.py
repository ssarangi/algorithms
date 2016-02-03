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
https://www.hackerrank.com/challenges/flowers
"""

import sys

def min_cost(K, costs):
    flowers = [0] * K
    costs = sorted(costs, reverse=True)
    total_cost = 0

    current_buyer = 0
    for i, cost in enumerate(costs):
        total_cost += cost * (flowers[current_buyer] + 1)
        flowers[current_buyer] += 1
        current_buyer += 1
        if current_buyer == K:
            current_buyer = 0

    return total_cost

def read(read_fn):
    N, K = [int(v) for v in read_fn().replace("\n", "").split(" ")]
    costs = [int(num) for num in read_fn().strip().replace("\n", "").split(" ")]

    return K, costs

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            K, costs = read(f.readline)
    else:
        K, costs = read(input)

    mc = min_cost(K, costs)
    print(mc)

if __name__ == "__main__":
    main()