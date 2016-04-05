# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return str([])
        
        serialized = []
        q = Queue()
        q.put((root.val, 0))
        
        while not q.empty():
            node, cn_idx = q.get()
            serialized.append(node.val)
            
            left_idx = 2 * cn_idx + 1
            right_idx = 2 * cn_idx + 2
            
            new_arr = [None] * right_idx
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        

# Your Codec object will be instantiated and called as such:
codec = Codec()

def create_tree():
    root = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    
    root.left = two
    root.right = three
    
    three.left = four
    three.right = five
    return root
    
root = create_tree()
codec.deserialize(codec.serialize(root))