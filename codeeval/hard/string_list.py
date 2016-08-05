import sys

def string_list_helper(s, curr_str, N, results):
    if len(curr_str) == N:
        results.add(curr_str)
        return
        
    for i in range(0, len(s)):
        c = s[i]
        newstr = curr_str + c
        string_list_helper(s, newstr, N, results)

def string_list(s, N):
    results = set()
    curr_str = ""
    string_list_helper(s, curr_str, N, results)
    results = sorted(results)
    return results

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.replace("\n", "")
        N, s = test.split(",")
        N = int(N)
        print(",".join(string_list(s, N)))