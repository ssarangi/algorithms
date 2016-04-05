# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _isValidBST(root, prev = None):
            if root is not None:
                is_valid_left, prev = _isValidBST(root.left)
                if not is_valid_left:
                    return False, prev
                    
                if prev is not None and root.val <= prev.val:
                    return False, prev
                    
                prev = root
                
                return _isValidBST(root.right, prev)
            
            return True, prev
        
        return _isValidBST(root)
        
def create_tree():
    root = TreeNode(10)
    left = TreeNode(5)
    right = TreeNode(15)
    right_right = TreeNode(20)
    right_left = TreeNode(6)
    
    root.left = left
    root.right = right
    root.right.left = right_left
    root.right_right = right_right
    
    root.left = left
    return root
    
soln = Solution()

root = create_tree()
print(soln.isValidBST(root)[0])

