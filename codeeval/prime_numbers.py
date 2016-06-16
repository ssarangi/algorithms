# https://www.codeeval.com/open_challenges/46/

import sys
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
    
def all_primes(range_max):
    result = []
    for i in range(2, range_max):
        if is_prime(i):
            result.append(i)
        
    return result

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        result = all_primes(int(test))
        print(",".join(str(i) for i in result))