# https://leetcode.com/problems/ransom-note/
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq = {}
        for c in magazine:
            freq[c] = 1 if c not in freq else freq[c] + 1
        
        for c in ransomNote:
            if c not in freq:
                return False
            elif freq[c] == 0:
                return False
            else:
                freq[c] -= 1
                
        return True
    
import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()
        
    def testCanConstruct(self):
        self.assertEqual(self.soln.canConstruct("a", "b"), False)
        self.assertEqual(self.soln.canConstruct("aa", "ab"), False)
        self.assertEqual(self.soln.canConstruct("aa", "aab"), True)
        
if __name__ == "__main__":
    unittest.main()