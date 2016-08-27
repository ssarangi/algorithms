# All the problems from the BST category

from queue import Queue
import sys


class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.v)


class BST:
    def __init__(self):
        self.root = None

    def __insert(self, node, v):
        if v < node.v:
            if node.left is not None:
                self.__insert(node.left, v)
            else:
                node.left = Node(v)
        else:
            if node.right is not None:
                self.__insert(node.right, v)
            else:
                node.right = Node(v)

    def insert(self, v, ):
        if self.root == None:
            self.root = Node(v)
        else:
            self.__insert(self.root, v)

    def __inorder(self, node, arr):
        if node.left is not None:
            self.__inorder(node.left, arr)

        arr.append(node.v)

        if node.right is not None:
            self.__inorder(node.right, arr)

    def inorder(self):
        arr = []
        self.__inorder(self.root, arr)
        return arr

    def inorder_iterative(self, k = -1):
        curr = self.root
        arr = []
        stack = []

        count = 0
        while curr is not None or len(stack) > 0:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                arr.append(node.v)
                count += 1
                if count == k:
                    return node.v

                curr = node.right

        return arr

    def __preorder(self, node, arr):
        arr.append(node.v)

        if node.left is not None:
            self.__preorder(node.left, arr)

        if node.right is not None:
            self.__preorder(node.right, arr)

    def preorder(self, arr):
        self.__preorder(self.root, arr)

    def __postorder(self, node, arr):
        if node.left is not None:
            self.__postorder(node.left, arr)

        if node.right is not None:
            self.__postorder(node.right, arr)

        arr.append(node.v)

    def postorder(self, arr):
        self.__postorder(self.root, arr)

    def levelorder(self):
        arr = []
        q = Queue()
        q.put((self.root, 0))

        curr_level = 0
        curr_level_arr = []
        while not q.empty():
            node, level = q.get()

            if level > curr_level:
                arr.append(curr_level_arr)
                curr_level = level
                curr_level_arr = []

            curr_level_arr.append(node.v)

            if node.left is not None:
                q.put((node.left, curr_level + 1))

            if node.right is not None:
                q.put((node.right, curr_level + 1))

        # Append the last level back
        arr.append(curr_level_arr)

        return arr

    def bottomupleveltraversal(self):
        arr = []
        stack = []
        q = Queue()
        q.put((self.root, 0))

        max_level = 0
        while not q.empty():
            node, level = q.get()
            max_level = max(max_level, level)

            stack.append((node, level))

            if node.right is not None:
                q.put((node.right, level + 1))

            if node.left is not None:
                q.put((node.left, level + 1))

        curr_level = max_level
        curr_level_arr = []

        while len(stack) > 0:
            node, level = stack.pop()

            if level < curr_level:
                arr.append(curr_level_arr)
                curr_level_arr = []
                curr_level = level

            curr_level_arr.append(node.v)

        arr.append(curr_level_arr)

        return arr

    def verticalOrder(self):
        levels = {}

        minlevel = sys.maxsize
        maxlevel = -sys.maxsize

        q = Queue()
        q.put((self.root, 0))

        while not q.empty():
            node, level = q.get()
            minlevel = min(minlevel, level)
            maxlevel = max(maxlevel, level)

            if level in levels:
                levels[level].append(node.v)
            else:
                levels[level] = [node.v]

            if node.left is not None:
                q.put((node.left, level - 1))

            if node.right is not None:
                q.put((node.right, level + 1))

        arr = []
        for i in range(minlevel, maxlevel + 1):
            arr.append(levels[i])

        return arr

    def __invertTree(self, node):
        if node.left is not None:
            self.__invertTree(node.left)

        if node.right is not None:
            self.__invertTree(node.right)

        node.left, node.right = node.right, node.left

    def invertTree(self):
        self.__invertTree(self.root)


import unittest


class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bst = BST()
        arr = [10, 5, 15, 2, 7, 1, 14, 17]

        for num in arr:
            cls.bst.insert(num)

    def testInorderTraversal(self):
        output = self.bst.inorder()
        self.assertEqual(output, [1, 2, 5, 7, 10, 14, 15, 17])

        output = self.bst.inorder_iterative()
        self.assertEqual(output, [1, 2, 5, 7, 10, 14, 15, 17])

    def testPreOrderTraversal(self):
        output = []
        self.bst.preorder(output)

        self.assertEqual(output, [10, 5, 2, 1, 7, 15, 14, 17])

    def testPostOrderTraversal(self):
        output = []
        self.bst.postorder(output)

        self.assertEqual(output, [1, 2, 7, 5, 14, 17, 15, 10])

    def testLevelOrderTraversal(self):
        output = self.bst.levelorder()
        self.assertEqual(output, [[10], [5, 15], [2, 7, 14, 17], [1]])

    def testBottomLevelOrderTraversal(self):
        output = self.bst.bottomupleveltraversal()
        self.assertEqual(output, [[1], [2, 7, 14, 17], [5, 15], [10]])

    def testVerticalOrder(self):
        output = self.bst.verticalOrder()
        self.assertEqual(output, [[1], [2], [5], [10, 7, 14], [15], [17]])

    def testInvertTree(self):
        orig_inorder = self.bst.inorder()
        orig_inorder.reverse()

        self.bst.invertTree()
        orig_invert = self.bst.inorder()
        self.bst.invertTree()

        self.assertEqual(orig_invert, orig_inorder)

    def testKthSmallestElement(self):
        el = self.bst.inorder_iterative(3)
        self.assertEqual(el, 5)


if __name__ == "__main__":
    unittest.main()