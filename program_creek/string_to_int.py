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
Implement atoi to convert a string to an integer.
1. null or empty string
2. white spaces
3. +/- sign
4. calculate real value
5. handle min & max
"""

# TODO: How to handle min & max
def atoi(string):
    string.strip(' ')
    assert(string !=  '' or string != None)

    # check the sign of the integer
    sign = 1
    if (string[0] == '-'):
        sign = -1
        string = string[1:]

    result = 0
    tens = 1
    decimal_present = -1
    for idx, c in enumerate(string):
        if c == '.':
            decimal_present = idx
        else:
            num = int(c)
            result = result * tens + num
            tens = 10

    if (decimal_present > -1):
        division_pt = 10 ** ((len(string) - 1) - decimal_present)
        result = result / division_pt

    result = result * sign
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(atoi("-3.46"), -3.46)

def main():
    print(atoi("-3.46"))

if __name__ == "__main__":
    main()
    unittest.main()