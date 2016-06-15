# https://www.codeeval.com/open_challenges/10/

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        inp = test.split(" ")
        last = int(inp[-1])
        inp = inp[:-1]
        
        if last <= len(inp):
            print(inp[len(inp) - last])