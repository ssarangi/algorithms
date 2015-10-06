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
Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic
if the characters in s can be replaced to get t.

For example,"egg" and "add" are isomorphic, "foo" and "bar" are not.
"""

def isomorphic(s, t):
    if len(s) != len(t):
        return False

    char_mapping = {}
    for idx, c_s in enumerate(s):
        c_t = t[idx]
        if c_s not in char_mapping:
            char_mapping[c_s] = c_t
        else:
            if char_mapping[c_s] != c_t:
                return False

    return True

def main():
    print(isomorphic("foo", "bar"))
    print(isomorphic("egg", "add"))

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(isomorphic("foo", "bar"), False)
        self.assertEqual(isomorphic("egg", "add"), True)

if __name__ == "__main__":
    main()
    unittest.main()