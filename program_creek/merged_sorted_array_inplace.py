"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.
"""


def merge_sorted_arrays(arr1, arr2):
    # Essentially the original array (arr1) should have that much space. But then we have to figure out the length of the array and stuff
    # So here I will create another array with the combined size and then do it inplace
    p1 = len(arr1) - 1
    arr1 += [0] * len(arr2)

    p2 = len(arr2) - 1

    curr_pos = len(arr1) - 1
    while p1 >= 0 or p2 >= 0:
        print(p1, p2)
        if p2 < 0 <= p1:
            arr1[curr_pos] = arr1[p1]
            p1 -= 1
        elif p1 < 0 <= p2:
            arr1[curr_pos] = arr2[p2]
            p2 -= 1
        elif arr1[p1] > arr2[p2]:
            arr1[curr_pos] = arr1[p1]
            p1 -= 1
        else:
            arr1[curr_pos] = arr2[p2]
            p2 -= 1

        curr_pos -= 1

    return arr1


import unittest


class Test(unittest.TestCase):
    def test(self):
        # self.assertEqual(merge_sorted_arrays([1,3,5,7,9], [2,4,6,8,10,11,12,13,14,15]), [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        # self.assertEqual(merge_sorted_arrays([1,3,5,6],[1,2,3,4,5,6]), [1, 1, 2, 3, 3, 4, 5, 5, 6, 6])
        self.assertEqual(merge_sorted_arrays([9, 10, 11, 12, 13], [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5, 9, 10, 11, 12, 13])


if __name__ == "__main__":
    unittest.main()