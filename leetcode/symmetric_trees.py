# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def symmetric(left, right):
            if left is None and right is None:
                return True

            # This is the case where either left or right is None.
            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            return symmetric(left.left, right.right) and \
                   symmetric(left.right, right.left)

        if root is None:
            return True

        return symmetric(root.left, root.right)

soln = Solution()


def create_tree():
    root = TreeNode(1)
    two_l = TreeNode(2)
    two_r = TreeNode(2)
    three_l = TreeNode(3)
    three_r = TreeNode(3)
    four_l = TreeNode(4)
    four_r = TreeNode(4)

    root.left = two_l
    root.right = two_r

    two_l.left = three_l
    two_l.right = four_l

    two_r.left = four_r
    two_r.right = three_r

    three_r.left = TreeNode(10)

    return root

root = create_tree()

print(soln.isSymmetric(root))
