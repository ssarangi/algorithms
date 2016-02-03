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

import sys

def min_units(weights):
    # diffs = [weights[i+1] - weights[i] for i in range(0, len(weights) - 1)]
    weights = sorted(weights)

    num_units = 1
    last_bought = weights[0]
    for w in weights:
        if abs(w - last_bought) > 4:
            last_bought = w
            num_units += 1

    return num_units

def read(read_fn):
    N = int(read_fn())
    weights = [int(item) for item in read_fn().replace('\n', '').split(" ")]
    return weights

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            weights = read(f.readline)
    else:
        weights = read(input)

    num_units = min_units(weights)
    print(num_units)

if __name__ == "__main__":
    main()