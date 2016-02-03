"""
The MIT License (MIT)

Copyright (c) <2015> <sarangis>

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
https://www.hackerrank.com/challenges/mark-and-toys
"""

def maximize_toys(prices, K):
    prices = sorted(prices)

    num_toys = 0
    total_price = 0
    idx = 0
    while True:
        total_price += prices[idx]
        if total_price > K:
            break
        idx += 1
        num_toys += 1

    return num_toys

import sys

def read(read_fn):
    N, K = [int(a) for a in (read_fn().split(" "))]
    prices = [int(price) for price in read_fn().replace('\n', '').split(" ")]

    return prices, K

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            prices, K = read(f.readline)
    else:
        prices, K = read(input)

    num_toys = maximize_toys(prices, K)
    print(num_toys)

if __name__ == "__main__":
    main()