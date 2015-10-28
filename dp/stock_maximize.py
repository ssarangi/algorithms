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
https://www.hackerrank.com/challenges/stockmax
"""

import sys

def stock_maximize(stock_prices):
    mystocks = 0
    transaction = []
    for idx, price in enumerate(stock_prices):
        if mystocks == 0:
            mystocks = 1
            transaction.append("b1")
        else:
            pass


def read(read_fn):
    test_cases = []
    T = int(read_fn())
    for i in range(0, T):
        N = int(read_fn())
        prices = read_fn()
        prices = [int(price) for price in prices.split(" ")]
        test_cases.append(prices)

    return test_cases

def main():
    if len(sys.argv) > 2:
        with open(sys.argv[1]) as f:
            test_cases = read(sys.argv[1])
    else:
        test_cases = read(input)

    for prices in test_cases:
        transactions = stock_maximize(prices)
        print(transactions)

if __name__ == "__main__":
    main()