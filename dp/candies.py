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
https://www.hackerrank.com/challenges/candies
"""

import sys

def candies(N, ratings):
    candies_given = [1] * N

    # 2 Pass solution. In the first pass we iterate over the ratings to find the max candies
    # have to hand out to preserve the condition.
    # The second pass is to then go for the less ones and figure out at what point we switch
    # from the max of prev to a lower number to minimize.
    # Step through the algorithm to see how it works
    for idx in range(1, len(ratings)):
        if ratings[idx - 1] < ratings[idx]:
            candies_given[idx] = candies_given[idx - 1] + 1

    for i in range(len(ratings) - 1, 0, -1):
        if ratings[i-1] > ratings[i]:
            candies_given[i-1] = max(candies_given[i-1], candies_given[i] + 1)

    return sum(candies_given)

def read_file(filename):
    with open(filename) as f:
        N = int(f.readline())
        ratings = []
        for i in range(0, N):
            rating = int(f.readline())
            ratings.append(rating)

        return N, ratings

def main():
    if len(sys.argv) > 1:
        N, ratings = read_file(sys.argv[1])
    else:
        N = int(input())
        ratings = []
        for i in range(0, N):
            ratings.append(int(input()))

    total = candies(N, ratings)
    print(total)

if __name__ == "__main__":
    main()