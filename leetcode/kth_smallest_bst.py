# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, v):
        if v < self.val:
            if self.left is None:
                self.left = TreeNode(v)
            else:
                self.left.insert(v)
        else:
            if self.right is None:
                self.right = TreeNode(v)
            else:
                self.right.insert(v)

    def __str__(self):
        return str(self.val)

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def k_largest(node, arr, k):
            if node.left is not None:
                k_largest(node.left, arr, k)

            if len(arr) == k:
                return

            arr.append(node.val)

            if node.right is not None:
                k_largest(node.right, arr, k)

        def k_smallest(node, arr, k):
            if node.right is not None:
                k_smallest(node.right, arr, k)

            if len(arr) == k:
                return

            arr.append(node.val)

            if node.left is not None:
                k_smallest(node.left, arr, k)

        tmp_arr = []
        k_smallest(root, tmp_arr, k)
        return tmp_arr[-1]

arr = [7, 5, 12, 3, 6, 1, 4, 9, 15, 8, 10, 13, 17]

root = TreeNode(7)

for i in range(1, len(arr)):
    root.insert(arr[i])

k = 3
soln = Solution()
print(soln.kthSmallest(root, k))