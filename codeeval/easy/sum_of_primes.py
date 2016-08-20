import sys

def sum_of_primes(limit):
    total = 0
    all_primes = set()
    for i in range(1, limit):
        is_prime = False
        
        if i == 1 or i == 2:
            total += i
            is_prime = True
            continue
        
        if not is_prime and i not in all_primes:
            cnum = i
            counter = 2
            while cnum < limit:
                all_primes.add(cnum)
                cnum *= counter
                counter += 1

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        limit = int(test)
        print(sum_of_primes(limit))