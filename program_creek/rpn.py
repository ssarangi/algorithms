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

# Reverse Polish Notation
# Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /.
# Each operand may be an integer or another expression.
# ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
# ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

import unittest
from program_creek.utils import Stack

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: int(x / y),
}


def evaluate_with_stack(rpn):
    stack = Stack()

    stack.push(int(rpn[0]))

    for i in rpn[1:]:
        if i in operators:
            y = stack.pop()
            x = stack.pop()
            result = operators[i](x, y)
            stack.push(result)
        else:
            stack.push(int(i))

    assert(stack.size() == 1)
    result = stack.pop()
    return result

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(evaluate_with_stack(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(evaluate_with_stack(["4", "13", "5", "/", "+"]), 6)

if __name__ == "__main__":
    unittest.main()