# https://www.codeeval.com/open_challenges/13/

import sys

def remove_characters(string, delimiters):
    ind_chr = set()
    for c in delimiters:
        ind_chr.add(c)
        
    new_str = ""
    for c in string:
        if c not in ind_chr:
            new_str += c
            
    return new_str

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        splitter_inp = test.split(",")
        string = splitter_inp[0]
        delimiters = splitter_inp[1].strip()
        new_str = remove_characters(string, delimiters)
        print(new_str)