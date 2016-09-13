def divide(numerator,denominator):
    pass

import unittest

class UnitTest(unittest.TestCase):
    def testDivide(self):
        self.assertEqual(divide(2, 5), "0.4")
        self.assertEqual(divide(-8, 7), "-1.[142857]")
        
if __name__ == "__main__":
    unittest.main()