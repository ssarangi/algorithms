import sys

def is_in_range(replaced_idx, i):
    for left, right in replaced_idx:
        if left <= i <= right:
            return True
    return False

def string_substitution(S, find_replace):
    replaced_idx = []

    for find_str, replace_str in find_replace:
        j = 0
        while j < len(S):
            if is_in_range(replaced_idx, j):
                j += 1
                continue

            curr_str = S[j: j + len(find_str)]

            if curr_str == find_str:
                S = S[0:j] + replace_str + S[j + len(find_str):]
                replaced_idx.append((j, j + len(find_str) - 1))
                break

            j += 1

    return S

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test.replace("\n", "")
        S, others = test.split(";")
        others = others.split(",")
        
        find_replace = []
        for i in range(0, len(others), 2):
            find_replace.append((others[i], others[i+1]))
        
        print(string_substitution(S, find_replace))