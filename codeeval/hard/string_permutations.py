# Write a program which prints all the permutations of a string in alphabetical order. We consider that 
# digits < upper case letters < lower case letters. The sorting should be performed in ascending order.
import sys

def permutations(s, curr_str, used_idx, results):
    if len(curr_str) == len(s):
        results.append(curr_str)
        return
    
    for i in range(0, len(s)):
        if i not in used_idx:
            # Insert i into the used idx to specify that we are using this idx
            used_idx.add(i)
            new_str = curr_str + s[i]
            permutations(s, new_str, used_idx, results)
            used_idx.remove(i)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.replace("\n", "")
        results = []
        used_idx = set()
        curr_str = ""
        permutations(test, curr_str, used_idx, results)
        results = sorted(results)
        print(",".join(results))