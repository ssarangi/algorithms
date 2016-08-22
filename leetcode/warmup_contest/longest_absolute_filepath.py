# https://leetcode.com/contest/1/problems/longest-absolute-file-path/

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # Split the string with '\n\t'. Then we will associate the strings
        names = input.split("\n\t")
        
    
import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()
        
    def testLengthLongestPath(self):
        self.assertEqual(self.soln.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"), 32)

if __name__ == "__main__":
    unittest.main()