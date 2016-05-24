# https://leetcode.com/problems/missing-number/
import unittest


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0
        while i < len(nums):
            if nums[i] < len(nums) and nums[i] != nums[nums[i]]:
                idx1 = i
                idx2 = nums[i]
                nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
            else:
                i += 1

        # Now iterate through the array and find out which index's don't match
        for idx, i in enumerate(nums):
            if i != idx:
                return idx

        return len(nums)


class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testMissingNumber(self):
        self.assertEqual(self.soln.missingNumber([0, 1, 3]), 2)
        self.assertEqual(self.soln.missingNumber([1]), 0)
        self.assertEqual(self.soln.missingNumber([]), 0)
        self.assertEqual(self.soln.missingNumber([0, 1]), 2)
        self.assertEqual(self.soln.missingNumber([2, 0]), 1)


if __name__ == "__main__":
    unittest.main()