"""
The MIT License (MIT)

Copyright (c) <2015> <sarangis>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import sys

def is_palindrome(string):
    if len(string) < 2:
        return False

    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False

        start += 1
        end -= 1

    return True

def get_permutations(N, chars):
    if N == 1:
        return chars

    prefix = chars
    final_permutations = []
    permutations = get_permutations(N-1, chars)

    for p in prefix:
        for perm in permutations:
            s = p + perm
            is_substring_palindrome = False
            for i in range(1, len(s)):
                substr = s[0:i+1]
                is_substring_palindrome |= is_palindrome(substr)
                if is_substring_palindrome:
                    break

            if not is_substring_palindrome:
                final_permutations.append(s)

    return final_permutations

def get_chars(M):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ac_chars = chars[0:M]
    res = []
    for c in ac_chars:
        res.append(c)
    return res

def compute_num_strings_old(N, M):
    chars = get_chars(M)
    permutations = get_permutations(N, chars)
    non_palindrome = len(permutations)
    return non_palindrome

def factorial(N):
    fact = 1
    while N > 1:
        fact *= N
        N -= 1

    return fact

def compute_combinations(M, N):
    combinations = factorial(M) / (factorial(N) * factorial(M-N))
    return combinations

def compute_permutations(M, N):
    permutations = factorial(M) // factorial(M - N)
    return permutations

def compute_fast_permutations(M, N):
    fact = 1
    for i in range(M, M - N, -1):
        fact *= i

    return fact

def compute_num_strings(N, M):
    # Figure out the number of strings we can create McN
    # combinations = compute_combinations(M)
    permutations = compute_fast_permutations(M, N)
    total_non_palindrome = permutations

    return total_non_palindrome

def read(read_fn):
    T = int(read_fn().replace("\n", ""))
    test_cases = []
    for i in range(0, T):
        N, M = [int(v) for v in read_fn().replace("\n", "").split(" ")]
        test_cases.append((N, M))

    return test_cases


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            test_cases = read(f.readline)
    else:
        test_cases = read(input)

    for t in test_cases:
        non_palindromes = compute_num_strings(t[0], t[1])
        print(non_palindromes % (10 ** 9 + 7))

if __name__ == "__main__":
    main()