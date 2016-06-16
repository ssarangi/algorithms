# https://www.codeeval.com/open_challenges/16/

import sys

def number_of_ones(num):
    num_ones = 0
    while num > 0:
        if num & 0x1 > 0:
            num_ones += 1
        num = num >> 1
    
    return num_ones

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num = int(test)
        print(number_of_ones(num))