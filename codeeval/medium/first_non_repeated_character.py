# https://www.codeeval.com/open_challenges/12/

import sys

def non_repeated_characters(word):
    seen = {}
    cc = ""
    for c in word:
        if c not in seen:
            seen[c] = 1
        else:
            seen[c] += 1
            
    for c in word:
        if seen[c] == 1:
            return c
            
    return ""

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        char = non_repeated_characters(test)
        print(char)