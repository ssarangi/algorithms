# https://leetcode.com/problems/minimum-height-trees/

class Solution(object):
    def create_graph(self, edges):
        node_paths = {}
        for edge in edges:
            if edge[0] not in node_paths:
                node_paths[edge[0]] = [edge[1]]
            else:
                node_paths[edge[0]].append(edge[1])
        
        return node_paths
        
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = self.create_graph(edges)
        

import unittest

class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testMaxArea(self):
        self.assertEqual(self.soln.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]), [1])
        self.assertEqual(self.soln.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]), [3, 4])

if __name__ == "__main__":
    unittest.main()