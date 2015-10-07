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
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

from program_creek.utils import Stack

def has_valid_parens(string):
    stack = Stack()
    closing_ops = [')','}',']']
    open_ops = ['(', '{', '[']

    open_close_dict = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for c in string:
        if c in closing_ops:
            top = stack.pop()
            if open_close_dict[top] != c:
                return False
        elif c in open_ops:
            stack.push(c)

    return stack.empty()

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(has_valid_parens("(ab)[124]"), True)
        self.assertEqual(has_valid_parens("[(ab])"), False)

def main():
    print(has_valid_parens("(ab)[124]"))
    print(has_valid_parens("[(ab])"))

if __name__ == "__main__":
    main()
    unittest.main()