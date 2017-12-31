# https://leetcode.com/problems/expression-add-operators/description/
class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        pass
    
import unittes

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testkSmallestPairs(self):
        self.assertEqual(self.soln.addOperators("123", 6), ["1+2+3", "1*2*3"])
        self.assertEqual(self.soln.addOperators("232", 8), ["2*3+2", "2+3*2"]) 
        self.assertEqual(self.soln.addOperators("105", 5), ["1*0+5","10-5"])
        self.assertEqual(self.soln.addOperators("00", 0), ["0+0", "0-0", "0*0"])
        self.assertEqual(self.soln.addOperators("3456237490", 9191), [])


if __name__ == "__main__":
    unittest.main()