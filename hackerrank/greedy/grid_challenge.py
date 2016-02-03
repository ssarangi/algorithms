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
https://www.hackerrank.com/challenges/grid-challenge
"""

# TODO: NOT_COMPLETE

import sys

def is_complete(arr):
    for y in range(0, len(arr)):
        for x in range(0, len(arr[0]) - 1):
            if arr[y][x] > arr[y][x+1]:
                return False

    for x in range(0, len(arr[0])):
        for y in range(0, len(arr) - 1):
            if arr[y][x] > arr[y+1][x]:
                return False

    return True

def lex_sort(arr):
    possible = "NO"

    # Sort all the rows
    for i, row in enumerate(arr):
        arr[i] = sorted(row)

    # # Sort all the columns
    # for i in range(0, len(arr[0])):
    #     col = []
    #     for j in range(0, len(arr)):
    #         col.append(arr[j][i])
    #
    #     col = sorted(col)
    #
    #     for j in range(0, len(col)):
    #         arr[j][i] = col[j]

    if is_complete(arr):
        possible = "YES"

    return possible

def read(read_fn):
    T = int(read_fn())
    alltestcases = []
    for i in range(0, T):
        N = int(read_fn())
        arr = []
        for j in range(0, N):
            string = read_fn().replace('\n', '')
            arr.append(string)

        alltestcases.append(arr)

    return alltestcases


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            alltestcases = read(f.readline)
    else:
        alltestcases = read(input)

    for testcase in alltestcases:
        res = lex_sort(testcase)
        print(res)

if __name__ == "__main__":
    main()