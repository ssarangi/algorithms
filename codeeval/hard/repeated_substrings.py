# Uses the http://www.geeksforgeeks.org/suffix-tree-application-3-longest-repeated-substring/
# Suffix tree construction.

import sys

def repeated_substring(string):
    

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        substr = repeated_substring(test)
        print(substr)