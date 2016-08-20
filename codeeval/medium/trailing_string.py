# https://www.codeeval.com/open_challenges/32/

import sys

def trailing_string(str1, str2):
    posn1 = len(str1) - 1
    posn2 = len(str2) - 1

    while posn2 >= 0:
        c1 = str1[posn1]
        c2 = str2[posn2]
        if str1[posn1] != str2[posn2]:
            return 0
        posn1 -= 1
        posn2 -= 1
            
    return 1

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        word_list = test.split(",")
        str1 = word_list[0].strip()
        str2 = word_list[1].strip()
        print(trailing_string(str1, str2))