# https://leetcode.com/contest/8/problems/sentence-screen-fitting/

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        pass

import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testAddStrings(self):
        self.assertEqual(self.soln.wordsTyping(["hello", "world"], 2, 8), 1)
        self.assertEqual(self.soln.wordsTyping(["a", "bcd", "e"], 3, 6), 2)
        self.assertEqual(self.soln.wordsTyping(["I", "had", "apple", "pie"], 4, 5), 1)

if __name__ == "__main__":
    unittest.main()