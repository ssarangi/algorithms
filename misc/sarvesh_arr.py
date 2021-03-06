# Given an array of N numbers consisting randomly of digits 0, 1, 2 create a
# sorted version of the array. Sorting is an easy enough solution with O(nlogn)
# However, O(n) is desired.

def arrange_helper(nums, number, p1, p2):
    while p1 < p2:
        while nums[p1] == number:
            p1 += 1

        while nums[p2] != number and p2 > p1:
            p2 -= 1

        nums[p1], nums[p2] = nums[p2], nums[p1]

    return p1


def arrange(nums):
    unique_nums = sorted(list(set(nums)))
    p1 = 0

    for i in range(0, len(unique_nums) - 1):
        p2 = len(nums) - 1
        # Do this is 2 passes
        # 1st pass will arrange all the 0's to the end
        p1 = arrange_helper(nums, unique_nums[i], p1, p2)
    
    return nums

import unittest
import random


class UnitTest(unittest.TestCase):
    def testArrangeNums(self):
        for _ in range(0, 10):
            arr = [random.randint(0, 2) for _ in range(0, 10)]
            self.assertEqual(arrange(arr), sorted(arr))
            
        for _ in range(0, 10):
            maxint = random.randint(0, 10)
            arr = [random.randint(0, maxint) for _ in range(0, 10)]
            self.assertEqual(arrange(arr), sorted(arr))


if __name__ == "__main__":
    unittest.main()