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
https://www.hackerrank.com/challenges/jim-and-the-orders
"""

import sys

def order_times(t_d):
    cust_time = []
    for item in t_d:
        cust_time.append((item[0] + item[1], item[2]))

    cust_time = sorted(cust_time, key=lambda item: item[0])

    order = []
    for time in cust_time:
        order.append(str(time[1]))

    return order

def read(read_fn):
    N = int(read_fn())
    t_d = []
    for i in range(0, N):
        t,d = read_fn().replace('\n', '').split(" ")
        t_d.append((int(t), int(d), i+1))

    return t_d

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            t_d = read(f.readline)
    else:
        t_d = read(input)

    order = order_times(t_d)
    print(" ".join(order))

if __name__ == "__main__":
    main()