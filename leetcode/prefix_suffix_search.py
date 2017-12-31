# Link: https://leetcode.com/problems/prefix-and-suffix-search/description/
class WordFilter:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words
        
    def brute_force(self, prefix, suffix):
        max_weight = -1
        for weight, word in enumerate(self.words):
            if word.startswith(prefix) and word.endswith(suffix):
                max_weight = weight
        
        return max_weight

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return self.brute_force(prefix, suffix)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = WordFilter(words)

    def testkSmallestPairs(self):
        self.assertEqual(self.soln.kSmallestPairs([1, 7, 11], [2, 4, 6], 3), [[1, 2], [1, 4], [1, 6]])
        self.assertEqual(self.soln.kSmallestPairs([1, 1, 2], [1, 2, 3], 2), [[1, 1], [1, 1]])
        self.assertEqual(self.soln.kSmallestPairs([1, 2], [3], 3), [[1, 3], [2, 3]])


if __name__ == "__main__":
    unittest.main()