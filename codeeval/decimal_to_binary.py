# https://www.codeeval.com/open_challenges/27/

import sys

def decimal_2_binary(num):
    if num == 0:
        return "0"
    
    binary = ""
    while num > 0:
        digit = num % 2
        binary = str(digit) + binary
        num = num // 2
        
    return binary

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num = int(test)
        print(decimal_2_binary(num))