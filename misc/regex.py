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

class Stack(list):
    def top(self):
        return self[-1]

    def empty(self):
        return len(self) == 0

class Regex:
    RegexOpPrecedence = {
        '(' : 1,
        '|' : 2,
        '.' : 3,
        '?' : 4,
        '*' : 4,
        '+' : 4,
        '^' : 5,
    }

    def __init__(self, pattern, op_precedence=None):
        self._pattern = pattern
        if op_precedence is None:
            self._precedence = Regex.RegexOpPrecedence
        else:
            self._precedence = op_precedence

    def compile(self):
        pass

    def get_right_associativity(self, c):
        prec = self._precedence.get(c, 6)
        return prec < 0

    def get_precedence(self, c):
        prec = self._precedence.get(c, 6)
        return abs(prec)

    def infix2postfix(self, input):
        stack = Stack()
        postfix = ""

        for c in input:
            if c == ')':
                # pop all items till we get the '('
                stack_top = ""
                while stack_top != "(":
                    stack_top = stack.pop()

                    if stack_top != '(':
                        postfix += stack_top
            elif c not in self._precedence:
                postfix += c
            else:
                stack.append(c)

        while not stack.empty():
            postfix += stack.pop()

        return postfix

def main():
    regex = Regex("mypattern")
    postfix = regex.infix2postfix("a+(b*c)")
    print(postfix)

if __name__ == "__main__":
    main()
