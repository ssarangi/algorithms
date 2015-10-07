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
Given a string containing just the characters '(' and ')', find the length of
the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.
Another example is ")()())", where the longest valid parentheses substring is "()()",
which has length = 4.
"""

from program_creek.utils import Stack

def longest_valid_parens(string):
    stack = Stack()

    longest = 0
    for c in string:
        if c == '(':
            stack.push(c)
        elif c == ')':
            if not stack.empty():
                top = stack.pop()
                if top == '(':
                    longest += 2

    return longest

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(longest_valid_parens("(()"), 2)
        self.assertEqual(longest_valid_parens(")()())"), 4)
        self.assertEqual(longest_valid_parens("((()))"), 6)

def main():
    print(longest_valid_parens("(()"))
    print(longest_valid_parens(")()())"))
    print(longest_valid_parens("((()))"))

if __name__ == "__main__":
    main()
    unittest.main()