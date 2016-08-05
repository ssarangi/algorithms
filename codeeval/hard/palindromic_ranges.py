import sys

def is_palindrome(number):
    # Extract the individual digits
    arr = []
    while number > 0:
        digit = number % 10
        arr.append(digit)
        number //= 10

    arr.reverse()

    p1 = 0
    p2 = len(arr) - 1

    while p1 <= p2:
        if arr[p1] != arr[p2]:
            return False

        p1 += 1
        p2 -= 1

    return True

def find_num_interesting_ranges(n1, n2):
    palindromes = set()

    for i in range(n1, n2 + 1):
        if is_palindrome(i):
            palindromes.add(i)

    interesting_ranges = 0
    for set_size in range(1, (n2 - n1 + 1) + 1):
        for j in range(n1, (n2 + 1 - set_size) + 1):
            num_pals = 0
            for k in range(j, j + set_size):
                if k in palindromes:
                    num_pals += 1
            
            if num_pals % 2 == 0:
                interesting_ranges += 1

    return interesting_ranges

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num1, num2 = test.split(" ")
        num1 = int(num1)
        num2 = int(num2)
        
        print(find_num_interesting_ranges(num1, num2))