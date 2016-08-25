# http://www.programcreek.com/2013/01/leetcode-longest-consecutive-sequence-java/

def longest_consecutive_sequence(arr):
    max_len = 0
    digit_count = {}

    for num in arr:
        curr_max_val = 1
        for i in range(-1, 2):
            if num + i not in digit_count:
                digit_count[num + i] = 0
            else:
                curr_max_val += digit_count[num + i]

        digit_count[num] = curr_max_val
        max_len = max(max_len, curr_max_val)

    return max_len


import unittest


class UnitTest(unittest.TestCase):
    def testMinimumSizeSubarray(self):
        self.assertEqual(longest_consecutive_sequence([100, 4, 200, 1, 2, 3]), 4)
        self.assertEqual(longest_consecutive_sequence([100, 4, 200, 3, 2, 1]), 4)
        self.assertEqual(longest_consecutive_sequence([100, 4, 200, 3, 2, 101]), 3)

if __name__ == "__main__":
    unittest.main()