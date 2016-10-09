# https://leetcode.com/contest/8/problems/add-strings/


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "":
            return int(num2)

        if num2 == "":
            return int(num1)

        p1 = len(num1) - 1
        p2 = len(num2) - 1

        greater = max(len(num1), len(num2))
        total = ""
        carry = 0

        while greater > 0:
            digit1 = int(num1[p1]) if p1 >= 0 else 0
            digit2 = int(num2[p2]) if p2 >= 0 else 0

            sum = carry + digit1 + digit2
            final_digit = sum % 10
            carry = sum // 10

            total = str(final_digit) + total
            greater -= 1

            p1 -= 1
            p2 -= 1

        if carry != 0:
            total = str(carry) + total

        return total

import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testAddStrings(self):
        self.assertEqual(self.soln.addStrings("112", "113"), "225")
        self.assertEqual(self.soln.addStrings("10", "5"), "15")
        self.assertEqual(self.soln.addStrings("1000", "5"), "1005")
        self.assertEqual(self.soln.addStrings("1", "9"), "10")

if __name__ == "__main__":
    unittest.main()