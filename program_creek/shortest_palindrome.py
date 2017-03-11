def shortest_palindrome(s):
    i = 0
    j = len(s) - 1

    while j >= 0:
        if s[i] == s[j]:
            i += 1
        j -= 1

    if i == len(s):
        return s

    suffix = s[i:]
    prefix = suffix[::-1]
    mid = shortest_palindrome(s[0:i])
    return prefix + mid + suffix


import unittest


class UnitTest(unittest.TestCase):
    def testShortestPalindrome(self):
        self.assertEqual(shortest_palindrome("aacecaaa"), "aaacecaaa")
        self.assertEqual(shortest_palindrome("death"), "htaedeath")
        self.assertEqual(shortest_palindrome("deathabchtaed"), "deathcbahtaedeathabchtaed")


if __name__ == "__main__":
    unittest.main()