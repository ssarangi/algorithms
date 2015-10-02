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

class Literal:
    def __init__(self, c):
        self.c = c

class Or:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

class Concat:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

class Repeat:
    def __init__(self, expr):
        self.expr = expr

class Plus:
    def __init__(self, expr):
        self.expr = expr

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

    def get_right_associativity(self, c):
        prec = self._precedence.get(c, 6)
        return prec < 0

    def get_precedence(self, c):
        prec = self._precedence.get(c, 6)
        return abs(prec)

    def format_regex(self, regex, result=""):
        all_operators = ['|', '?', '+', '*', '^']
        binary_operators = ['^', '|']

        if not regex:
            return result

        c1 = regex[0]
        c2 = ' '
        if len(regex) >= 2:
            c2 = regex[1]

        tmp = ''
        if c1 != '(' and c2 != ')' and c2 != ' ' and (c2 not in all_operators) and (c1 not in binary_operators):
            tmp = '.'

        return self.format_regex(regex[1:], result + c1 + tmp)


    def infix2postfix(self, input):
        """
        a.b*|c+.d transforms to ab*.c+d.|
        :param input:
        :return:
        """
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

    def postfix2tree(self, postfix):
        stack = []

        for c in postfix:
            if c == '.':
                rhs = stack.pop()
                lhs = stack.pop()
                concat_expr = Concat(lhs, rhs)
                stack.append(concat_expr)
            elif c == '*':
                top_expr = stack.pop()
                repeat_expr = Repeat(top_expr)
                stack.append(repeat_expr)
            elif c == '+':
                top_expr = stack.pop()
                plus_expr = Plus(top_expr)
                stack.append(plus_expr)
            elif c == '|':
                rhs = stack.pop()
                lhs = stack.pop()
                or_expr = Or(lhs, rhs)
                stack.append(or_expr)
            else:
                expr = Literal(c)
                stack.append(expr)

        assert(len(stack) == 1)
        return stack.pop()

    class Consume:
        def __init__(self, c, out):
            self.c = c
            self.out = out

    class Split:
        def __init__(self, out1, out2):
            self.out1 = out1
            self.out2 = out2

    class Placeholder:
        def __init__(self, pointing_to):
            self.pointing_to = pointing_to

    class Match:
        pass

    def regex2NFA(self, regex, nextState = Match()):
        if isinstance(regex, Literal):
            return Regex.Consume(regex.c, nextState)
        elif isinstance(regex, Concat):
            return self.regex2NFA(regex.lhs, self.regex2NFA(regex.rhs, nextState))
        elif isinstance(regex, Or):
            return Regex.Split(self.regex2NFA(regex.lhs, nextState), self.regex2NFA(regex.rhs, nextState))
        elif isinstance(regex, Repeat):
            placeholder = Regex.Placeholder(None)
            split = Regex.Split(self.regex2NFA(regex.expr, placeholder), nextState)
            placeholder.pointing_to = split
            return placeholder
        elif isinstance(regex, Plus):
            return self.regex2NFA(Concat(regex.expr, Repeat(regex.expr)), nextState)

    def evaluate_nfa_recursive(self, root, string_to_match):
        if isinstance(root, Regex.Match):
            if not string_to_match:
                return True
            else:
                return False
        elif isinstance(root, Regex.Split):
            self.evaluate_nfa_recursive(root.out1, string_to_match) | self.evaluate_nfa_recursive(root.out2, string_to_match)
        elif isinstance(root, Regex.Consume):
            if not string_to_match:
                return False
            elif root.c != string_to_match[0]:
                return False
            else:
                self.evaluate_nfa_recursive(root.out, string_to_match[1:])
        elif isinstance(root, Regex.Placeholder):
            self.evaluate_nfa_recursive(root.pointing_to, string_to_match)


    def compile(self):
        formatted_regex = self.format_regex("ab*|c+d")
        postfix = self.infix2postfix(formatted_regex)
        tree = self.postfix2tree(postfix)
        self._nfa = self.regex2NFA(tree)

    def match(self, string_to_match):
        return self.evaluate_nfa_recursive(self._nfa, string_to_match)

def main():
    regex = Regex("ab*|c+d")
    regex.compile()
    match = regex.match("cccccccccccccccd")
    print(match)

if __name__ == "__main__":
    main()
