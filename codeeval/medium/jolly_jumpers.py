# https://www.codeeval.com/open_challenges/43/submit/


import sys

def is_jolly_jumper(n, num_list):
    all_nums = set()
    
    for i in range(0, len(num_list) - 1):
        diff = abs(num_list[i+1] - num_list[i])
        all_nums.add(diff)
        
    for i in range(1, n):
        if i not in all_nums:
            return False
            
    return True

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        num_list = [int(i) for i in test.split(" ")]
        n = num_list[0]
        num_list = num_list[1:]
        is_jolly = is_jolly_jumper(n, num_list)
        if is_jolly:
            print("Jolly")
        else:
            print("Not jolly")