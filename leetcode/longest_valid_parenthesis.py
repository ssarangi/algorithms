class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass
    
import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()
        
    def testLongestValidParenthesis(self):
        self.assertEqual(self.soln.longestValidParentheses("(()"), 2)
        self.assertEqual(self.soln.longestValidParentheses(")()())"), 4)

if __name__ == "__main__":
    unittest.main()