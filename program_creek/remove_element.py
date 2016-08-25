def remove_element(arr, elm):
    i = 0
    j = 0

    while j < len(arr):
        if arr[j] != elm:
            arr[i] = arr[j]
            i += 1

        j += 1

    return arr


import unittest


class UnitTest(unittest.TestCase):
    def testMinimumSizeSubarray(self):
        self.assertEqual(remove_element([2, 3, 1, 2, 4, 3], 2), [3, 1, 4, 3, 4, 3])


if __name__ == "__main__":
    unittest.main()