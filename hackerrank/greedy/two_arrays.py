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
https://www.hackerrank.com/challenges/two-arrays
"""

def permutation_exists(A, B, K):
    A = sorted(A, reverse=True)
    B = sorted(B)

    idx = 0
    for elA in A:
        diff = K - elA
        if diff > B[-1]:
            return "NO"

        while idx < len(B):
            if B[idx] + elA >= K:
                B.remove(B[idx])
                break
            idx += 1

    return "YES"

import sys

def read(read_fn):
    T = int(read_fn())
    test_cases = []
    for i in range(0, T):
        N, K = [int(a) for a in read_fn().replace('\n', '').split(" ")]
        A = [int(item) for item in read_fn().replace('\n', '').split(" ")]
        B = [int(item) for item in read_fn().replace('\n', '').split(" ")]
        test_cases.append([A, B, K])

    return test_cases

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            testcases = read(f.readline)
    else:
        testcases = read(input)

    for t in testcases:
        exists = permutation_exists(t[0], t[1], t[2])
        print(exists)

if __name__ == "__main__":
    main()