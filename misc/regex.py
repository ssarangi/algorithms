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
        return len(self) > 0

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

    def infix2postfix_old(self, input, op_stack, op_precedence, postfix_prev_iter):
        postfix = postfix_prev_iter
        stack = op_stack

        if not input:
            return postfix + "".join(stack)

        c = input[0]

        if c == '(':
            stack.append(c)
        elif c == ')':
            stack_elms_to_pop = [el for el in stack if el != '(']
            postfix += "".join(stack_elms_to_pop)
            stack = stack[len(postfix):]
        else:
            c_precedence = self.get_precedence(c, op_precedence)
            stack_to_take = [x for x in stack if self.get_precedence(x, op_precedence) >= c_precedence]
            postfix += "".join(stack_to_take)
            stack = stack[len(stack) - len(stack_to_take):]
            stack.append(c)

        return self.infix2postfix(input[1:], stack, op_precedence, postfix)


    def infix2postfix(self, input):
        stack = Stack()
        postfix = ""
        stack.append(input[0])

        for c in input[1:]:
            top = stack.top()
            if self.get_precedence(c) > self.get_precedence(top):
                op = stack.pop()
                lhs = stack.pop()
                rhs = c
                postfix += lhs + rhs + op
                stack.append(postfix)
            else:
                stack.append(c)

        return "".join(stack)

def main():
    regex = Regex("mypattern")
    postfix = regex.infix2postfix("a+(b*c)")
    print(postfix)

if __name__ == "__main__":
    main()
