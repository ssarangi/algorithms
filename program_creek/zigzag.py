# http://www.programcreek.com/2013/01/leetcode-longest-consecutive-sequence-java/

def zigzag(string, numrows):
    arr = [[] for _ in range(0, numrows)]
    
    row = 0
    dir = 1
    for i in range(0, len(string)):
        arr[row].append(string[i])
        if row == numrows:
            dir = -1
        elif row == 0:
            dir = 1
        
        row += dir
        
    newstr = ""
    for i in range(0, numrows):
        newstr += arr[i]

import unittest


class UnitTest(unittest.TestCase):
    def testMinimumSizeSubarray(self):
        self.assertEqual(zigzag("PAYPALISHIRING"), 3)

if __name__ == "__main__":
    unittest.main()