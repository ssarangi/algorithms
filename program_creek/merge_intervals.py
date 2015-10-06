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
    kwargs = list(kwargs)
    idx = 0
    while idx < len(kwargs) - 1:
        interval_1 = kwargs[idx]
        interval_2 = kwargs[idx + 1]
        if interval_1[1] >= interval_2[0]:
            if interval_1[1] <= interval_2[1]:
                interval_1.remove(interval_1[1])
                interval_1.append(interval_2[1])
            kwargs.remove(interval_2)
        else:
            idx += 1

    return [kwargs]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge_intervals([1,3],[2,6],[8,10],[15,18]), [[1,6],[8,10],[15,18]])
        self.assertEqual(merge_intervals([1,4],[3,5],[2,4],[6,10]), [[1,5],[6,10]])

def main():
    merge_intervals([1,3],[2,6],[8,10],[15,18])
    merge_intervals([1,4],[3,5],[2,4],[6, 10])

if __name__ == "__main__":
    unittest.main()