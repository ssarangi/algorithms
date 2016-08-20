# https://www.codeeval.com/open_challenges/41/submit/

import sys

def array_absurdity(arr, N):
    p1 = 0
    while p1 < len(arr):
        print(arr)
        if arr[p1] != p1:
            if arr[arr[p1]] == arr[p1]:
                return arr[p1]
            else:
                arr[p1], arr[arr[p1]] = arr[arr[p1]], arr[p1]
        else:
            p1 += 1
    

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        splitted_inp = test.split(";")
        N = int(splitted_inp[0])
        num_list = splitted_inp[1]
        num_list = [int(i) for i in num_list.split(",")]
        duplicated = array_absurdity(num_list, N)
        print(duplicated)