# https://www.codeeval.com/open_challenges/34/

import sys

def number_pairs(num_list, sum_v):
    results = []
    p1 = 0
    p2 = len(num_list) - 1
    
    while p1 < p2:
        d1 = num_list[p1]
        d2 = num_list[p2]
        
        if d1 + d2 == sum_v:
            results.append((d1, d2))
            p1 += 1
            p2 -= 1
        elif d1 + d2 > sum_v:
            p2 -= 1
        else:
            p1 += 1
            
    return results

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        splitted = test.split(";")
        sum_v = int(splitted[1])
        num_list = splitted[0]
        num_list = [int(i) for i in num_list.split(",")]
        
        num_pairs = number_pairs(num_list, sum_v)
        if len(num_pairs) == 0:
            print("NULL")
        else:
            s = ""
            for pair in num_pairs:
                s += ",".join(str(i) for i in pair)
                s += ";"
                
            s = s[:-1]
            print(s)