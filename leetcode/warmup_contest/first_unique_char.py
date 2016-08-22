# https://leetcode.com/contest/1/problems/first-unique-character-in-a-string/
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # First pass through the string to find out the frequencies of the chars
        char_freq = {}
        for c in s:
            if c in char_freq:
                char_freq[c] += 1
            else:
                char_freq[c] = 1
                
                
        # 2nd pass... Go through the characters again to find the firtst unique-char
        for idx, c in enumerate(s):
            if char_freq[c] == 1:
                return idx
                
        return -1
    
import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()
        
    def testFirstUniqueChar(self):
        self.assertEqual(self.soln.firstUniqChar("leetcode"), 0)
        self.assertEqual(self.soln.firstUniqChar("loveleetcode"), 2)
        
if __name__ == "__main__":
    unittest.main()