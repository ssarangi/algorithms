# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

import heapq


class MinHeap:
    def __init__(self):
        self.data = []

    def add(self, v, idx1, idx2):
        heapq.heappush(self.data, (-v, [idx1, idx2]))

    def length(self):
        return len(self.data)

    def pop(self):
        return heapq.heappop(self.data)

    def top(self):
        return -1 * self.data[0][0]

    def empty(self):
        return len(self.data) == 0


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        minheap = MinHeap()
        for n1 in nums1:
            for n2 in nums2:
                s = n1 + n2
                add_el = True
                if minheap.length() == k:
                    # Remove the max element
                    if minheap.top() > s:
                        minheap.pop()
                    else:
                        add_el = False

                if add_el:
                    minheap.add(s, n1, n2)

        # Now pop all the elements of the min heap
        results = []
        while not minheap.empty():
            results.insert(0, minheap.pop()[1])

        return results


import unittest


class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testkSmallestPairs(self):
        self.assertEqual(self.soln.kSmallestPairs([1, 7, 11], [2, 4, 6], 3), [[1, 2], [1, 4], [1, 6]])
        self.assertEqual(self.soln.kSmallestPairs([1, 1, 2], [1, 2, 3], 2), [[1, 1], [1, 1]])
        self.assertEqual(self.soln.kSmallestPairs([1, 2], [3], 3), [[1, 3], [2, 3]])


if __name__ == "__main__":
    unittest.main()