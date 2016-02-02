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

def lex_sort(arr):
    possible = "NO"

    # figure out the 1st Row and 1st Column
    row = []
    col = []

    for c in arr[0]:
        row.append(c)

    for c in arr:
        col.append(c[0])

    row = sorted(row)
    col = sorted(col)

    if row[0] < col[0]:
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