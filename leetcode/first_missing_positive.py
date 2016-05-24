# https://leetcode.com/problems/first-missing-positive/

import unittest


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1

        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                idx1 = i
                idx2 = nums[i] - 1
                nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
            else:
                i += 1

        # Now iterate through the array and find out which index's don't match
        for idx, i in enumerate(nums):
            if i != idx + 1:
                return idx + 1

        return len(nums) + 1

class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testFirstMissingPositive(self):
        self.assertEqual(self.soln.firstMissingPositive([1, 2, 0]), 3)
        self.assertEqual(self.soln.firstMissingPositive([3, 4, -1, 1]), 2)
        self.assertEqual(self.soln.firstMissingPositive([1]), 2)


if __name__ == "__main__":
    unittest.main()