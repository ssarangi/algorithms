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
You are given an array of real numbers
i.e. the numbers can be positive, negative ...
find the sub array with the max product
"""

import sys

def max_product(arr):
    all_zeros = True
    all_negative = True
    max_pos_prod = [1] * len(arr)
    max_cum_prod = [1] * len(arr)

    val_to_set = arr[0]
    if arr[0] == 0:
        val_to_set = 1

    max_pos_prod[0] = val_to_set
    max_cum_prod[0] = val_to_set
    maxv = -sys.maxsize

    for i, el in enumerate(arr):
        if el != 0:
            all_zeros = False

        if el > 0:
            all_negative = False

        if i == 0:
            continue

        if el != 0:
            max_cum_prod[i] = max_cum_prod[i-1] * el
        else:
            max_cum_prod[i] = 1

        maxv = max(maxv, max_cum_prod[i])
        if el < 0:
            # Check to see if we have a previous pos sum till now on the cumulative
            # array
            max_pos_prod[i] = 1
        else:
            max_pos_prod[i] = el * max_pos_prod[i-1]

        maxv = max(maxv, max_pos_prod[i])

    if all_zeros:
        maxv = 0
    elif all_negative:
        maxv = max_cum_prod[-1]

    return maxv

def main():
    testcase1 = [1, 2, 3, -4]
    testcase2 = [-3, 2, 3, 4, -5]
    testcase3 = [0, -3, -4, 1, 2, 3]
    testcase4 = [0,0,0,0,0,0]
    testcase5 = [-1,-1,-1,-1,-1]
    testcase6 = [-1,-1,-1,-1,-1,4]

    print(max_product(testcase6))
    assert max_product(testcase1) == 6
    assert max_product(testcase2) == 360
    assert max_product(testcase3) == 72
    assert max_product(testcase4) == 0
    assert max_product(testcase5) == -1
    assert max_product(testcase6) == 4

if __name__ == "__main__":
    main()