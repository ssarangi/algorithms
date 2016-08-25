def minimum_size_subarray(arr, s):
    p1 = 0
    p2 = 0

    min_len = len(arr)

    if len(arr) == 1:
        if arr[0] >= s:
            return 1
        else:
            return 0

    # Initialize with the curr_sum
    curr_sum = arr[0]
    while p1 < len(arr):
        if curr_sum >= s:
            # See if this length is the max or not
            length = p2 - p1 + 1
            min_len = min(min_len, length)

            # Move the left pointer
            curr_sum -= arr[p1]
            p1 += 1
        else:
            # Move the right pointer and update the current sum
            if p2 == len(arr) - 1:
                break

            p2 += 1
            curr_sum += arr[p2]

    return min_len


import unittest


class UnitTest(unittest.TestCase):
    def testMinimumSizeSubarray(self):
        self.assertEqual(minimum_size_subarray([2, 3, 1, 2, 4, 3], 7), 2)


if __name__ == "__main__":
    unittest.main()