# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import heapq


class MinHeap:
    def __init__(self):
        self.data = []

    def add(self, v, idx1, idx2):
        heapq.heappush(self.data, (v, [idx1, idx2]))

    def length(self):
        return len(self.data)

    def pop(self):
        return heapq.heappop(self.data)

    def top(self):
        return self.data[0][0]

    def empty(self):
        return len(self.data) == 0


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        minheap = MinHeap()

        for idx, el in enumerate(matrix[0]):
            minheap.add(el, idx, 0)

        popped_el = -1
        for i in range(0, k):
            # Pop the min element and then find the next element from the same column
            popped_el, [x, y] = minheap.pop()

            if i+1 < k:
                if y + 1 < len(matrix):
                    next_el = matrix[y + 1][x]
                    minheap.add(next_el, x, y + 1)

        return popped_el


import unittest


class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testkthSmallest(self):
        self.assertEqual(self.soln.kthSmallest([ \
            [1, 5, 9], \
            [10, 11, 13], \
            [12, 13, 15] \
            ], 8), 13)

        self.assertEqual(self.soln.kthSmallest([[-5]], 1), -5)

        self.assertEqual(self.soln.kthSmallest([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 1), 1)
        self.assertEqual(self.soln.kthSmallest([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 2), 3)
        self.assertEqual(self.soln.kthSmallest([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 3), 5)
        self.assertEqual(self.soln.kthSmallest([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 4), 6)
        self.assertEqual(self.soln.kthSmallest([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 5), 7)
        self.assertEqual(self.soln.kthSmallest(
            [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19], [12, 14, 16, 18, 20], [21, 22, 23, 24, 25]], 8),
            8)

        self.assertEqual(self.soln.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13)
        self.assertEqual(self.soln.kthSmallest([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 25), 25)


if __name__ == "__main__":
    unittest.main()