# https://www.hackerrank.com/contests/hourrank-18/challenges/super-six-substrings

def get_consecutive_substrings(s):
    substrings = []

    end = len(s)
    for start in range(0, end):
        for end_pos in range(start+1, end+1):
            substring = s[start:end_pos]
            if len(substring) == 1 or (len(substring) > 1 and substring[0] != '0'):
                substrings.append(substring)

    return substrings

def divisible_by_three(s):
    sum = 0
    for c in s:
        sum += int(c)
    if sum % 3 == 0:
        return True

    return False

def divisible_by_two(s):
    last_char = s[-1]
    if last_char == '0' or last_char == '2' or last_char == '4' or last_char == '6' or last_char == '8':
        return True

    return False

def divisible_by_six(s):
    if divisible_by_three(s) and divisible_by_two(s):
        return True

    return False

def supersix_strings(s):
    s = "4806"
    substrings = get_consecutive_substrings(s)

    total_count = 0
    for s in substrings:
        total_count += int(divisible_by_six(s))

    return total_count

import unittest


class UnitTest(unittest.TestCase):
    def testkSmallestPairs(self):
        self.assertEqual(supersix_strings("4806"), 5)


if __name__ == "__main__":
    unittest.main()