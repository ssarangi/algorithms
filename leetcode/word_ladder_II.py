import unittest

class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        wordList = set(wordList)
        
    
class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testIsNumber(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        result = [
            ["hit","hot","dot","dog","cog"],
            ["hit","hot","lot","log","cog"]
        ]
        
        self.assertEqual(self.soln.findLadders(beginWord, endWord, wordList), result)
        
if __name__ == "__main__":
    unittest.main()