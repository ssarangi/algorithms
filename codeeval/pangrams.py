# https://www.codeeval.com/open_challenges/37/

import sys

def find_missing_chars(sentence):
    hash_t = 0
    for c in sentence:
        if c == ' ' or c == '\n':
            continue
        
        c = c.lower()
        ascii = ord(c) - ord('a')
        
        if ascii < 0:
            continue
        
        hash_t |= (1 << ascii)
        
    missing_chars = ""
    for i in range(0, 26):
        if hash_t & (1 << i) == 0:
            missing_chars += chr(ord('a') + i)
            
    if missing_chars == "":
        return "NULL"
    else:
        return missing_chars

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        missing_chars = find_missing_chars(test)
        print(missing_chars)