import unittest

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        ctr = 0
        seen_decimal = False
        seen_exp = False
        seen_digits = False
        seen_plus = False
        seen_minus = False
        for i, c in enumerate(s):
            if (c == '-' or c == '+') and (i == 0 or seen_exp is True):
                if c == '+' and seen_plus is True:
                    return False
                elif c == '-' and seen_minus is True:
                    return False
                seen_plus = True if c == '+' else False
                seen_minus = True if c == '-' else False
                seen_digits = False
                continue
            elif c == ".":
                if seen_decimal is True or seen_exp is True:
                    return False
                seen_decimal = True
            elif c == "e":
                if seen_exp is True or seen_digits is False:
                    return False
                seen_exp = True
                seen_digits = False
            elif ord(c) < 48 or ord(c) > 57:
                return False
            else:
                seen_digits = True
                seen_plus = False
                seen_minus = False
        
        if seen_digits is False:
            return False
            
        return True

class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testIsNumber(self):
        self.assertEqual(self.soln.isNumber("0"), True)
        self.assertEqual(self.soln.isNumber(" 0.1 "), True)
        self.assertEqual(self.soln.isNumber("abc"), False)
        self.assertEqual(self.soln.isNumber("1 a"), False)
        self.assertEqual(self.soln.isNumber("2e10"), True)
        self.assertEqual(self.soln.isNumber("e"), False)
        self.assertEqual(self.soln.isNumber("e9"), False)
        self.assertEqual(self.soln.isNumber("0e"), False)
        self.assertEqual(self.soln.isNumber("3."), True)
        self.assertEqual(self.soln.isNumber("-1."), True)
        self.assertEqual(self.soln.isNumber("+.8"), True)
        self.assertEqual(self.soln.isNumber("6e6.5"), False)
        self.assertEqual(self.soln.isNumber(" 005047e+6"), True)
        self.assertEqual(self.soln.isNumber("459277e38+"), False)
        self.assertEqual(self.soln.isNumber("2e+60++604"), False)
        self.assertEqual(self.soln.isNumber(" -.7e+0435"), True)
        self.assertEqual(self.soln.isNumber("+42e+76125"), True)
        
if __name__ == "__main__":
    unittest.main()