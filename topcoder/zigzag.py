# https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493

class ZigZag:
    def longestZigZag(self, sequence):
        if len(sequence) == 0:
            return 1

        dp = [0] * len(sequence)
        diff = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
        print(diff)

        return 0

import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = ZigZag()
    
    def testZigZag(self):
        self.assertEqual(self.soln.longestZigZag([1, 7, 4, 9, 2, 5]), 6)
        self.assertEqual(self.soln.longestZigZag([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]), 7)
        self.assertEqual(self.soln.longestZigZag([44]), 1)
        self.assertEqual(self.soln.longestZigZag([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2)
        self.assertEqual(self.soln.longestZigZag([70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]), 8)
        self.assertEqual(self.soln.longestZigZag([374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
                                                  600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
                                                  67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
                                                  477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
                                                  249, 22, 176, 279, 23, 22, 617, 462, 459, 244]), 36)
                                                  
if __name__ == "__main__":
    unittest.main()