# /usr/bin/python
import sys

ops = {
    '+' : lambda x, y: x + y,
    '*' : lambda x, y: x * y,
    '/' : lambda x, y: x / y
}

def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False

    return True

def evaluate(tokens):
    s = []
    for t in tokens:
        if t == '*' or t == '/' or t == '+':
            s.append(t)
        else:
            if not is_number(s[-1]):
                s.append(float(t))
            else:
                n1 = float(t)
                n2 = float(s.pop())
                op = s.pop()
                v = ops[op](n2, n1)
                s.append(v)

    res = s.pop()
    return int(res)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        tokens = test.split(" ")
        print(evaluate(tokens))