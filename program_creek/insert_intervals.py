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
Given a set of non-overlapping & sorted intervals, insert a new interval into the intervals (merge if necessary).

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

def insert_interval(interval_to_add, *kwargs):
    kwargs = list(kwargs)
    idx = 0
    while idx < len(kwargs) - 1:
        interval = kwargs[idx]
        if interval[1] > interval_to_add[0] and interval[1] < interval_to_add[1]:
            interval[1] = interval_to_add[1]
        else:
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
        self.assertEqual(insert_interval([2,5],[1,3],[6,9]), [[1,5],[6,9]])
        self.assertEqual(insert_interval([4,9],[1,2],[3,5],[6,7],[8,10],[12,16]), [[1,2],[3,10],[12,16]])

def main():
    insert_interval([2,5],[1,3],[6,9])
    insert_interval([4,9],[1,2],[3,5],[6,7],[8,10],[12,16])

if __name__ == "__main__":
    main()
    unittest.main()