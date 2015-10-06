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
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

def merge_intervals(*kwargs):
    intervals = []
    intervals.append(kwargs[0][0])
    for i in range(0, len(kwargs) - 2):
        interval1 = kwargs[i]
        interval2 = kwargs[i+1]

        if interval2[0] <= interval1[1]:
            intervals.append(interval2[1])

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge_intervals([1,3],[2,6],[8,10],[15,18]), [[1,6],[8,10],[15,18]])

def main():
    pass

if __name__ == "__main__":
    pass