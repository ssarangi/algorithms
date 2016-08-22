# https://leetcode.com/contest/1/problems/lexicographical-numbers/

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = set()
        for i in range(1, 10):
            powers = 0
            
            while True:
                power_val = pow(10, powers)
                start_val = i * power_val
                if start_val > n:
                    break
                
                for j in range(i * start_val, min(n, start_val + power_val)):
                    result.add(j)

        return list(result)

import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()
        
    def testLexicalOrder(self):
        self.assertEqual(self.soln.lexicalOrder(13), [1,10,11,12,13,2,3,4,5,6,7,8,9])
        
        
if __name__ == "__main__":
    unittest.main()