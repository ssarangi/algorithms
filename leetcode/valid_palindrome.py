# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True

        s = s.lower()
        p1 = 0
        p2 = len(s) - 1
        
        while p1 < p2:
            while p1 < p2 and not s[p1].isalnum() or s[p1] == ' ':
                p1 += 1
                
            while p2 > p1 and not s[p2].isalnum() or s[p2] == ' ':
                p2 -= 1
            
            if s[p1] != s[p2]:
                return False
                
            p1 += 1
            p2 -= 1
                
        return True
    
import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()
        
    def testIsPalindrome(self):
        self.assertEqual(self.soln.isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(self.soln.isPalindrome(".,"), True)
        self.assertEqual(self.soln.isPalindrome("0P"), False)
        self.assertEqual(self.soln.isPalindrome("Telegram\n\
Margelet!"), True)

if __name__ == "__main__":
    unittest.main()