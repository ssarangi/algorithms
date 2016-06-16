# https://www.codeeval.com/open_challenges/45

import sys

def check_palindrome_and_sum(num):
    total_digits = 0
    arr = []
    while num > 0:
        digit = num % 10
        total_digits += 1
        arr.append(digit)
        num = num // 10
    
    is_palindrome = True
    # Now the arr has the individual elemenets
    p1 = 0
    p2 = len(arr) - 1
    
    while p1 < p2:
        if arr[p1] != arr[p2]:
            is_palindrome = False
            break
        p1 += 1
        p2 -= 1
        
    # Now find the reverse of the digit
    ten_pow = 0
    reversed_num = 0
    while len(arr) > 0:
        digit = arr.pop()
        reversed_num += digit * pow(10, ten_pow)
        ten_pow += 1
        
    return reversed_num, is_palindrome

def compute_soln(num):
    iteration = 0
    
    is_palindrome = False
    while iteration <= 100 and not is_palindrome:
        reversed_num, is_palindrome = check_palindrome_and_sum(num)
        if not is_palindrome:
            num = reversed_num + num
            iteration += 1
        
    return iteration, num

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num = int(test)
        iteration, palindrome = compute_soln(num)
        print(iteration, palindrome)