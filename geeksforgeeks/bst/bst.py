"""
The MIT License (MIT)

Copyright (c) <2015> <sarangis>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import math

class Node:
    def __init__(self, data, parent=None):
        self.__data = data
        self.__left = None
        self.__right = None
        self.__parent = parent

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, val):
        self.__data = val

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, val):
        self.__left = val

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, val):
        self.__right = val

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, p):
        self.__parent = p

    def __str__(self):
        return str(self.__data)

    def add(self, v):
        if v < self.__data:
            if self.__left is None:
                self.__left = Node(v, self)
            else:
                self.__left.add(v)
        elif v > self.__data:
            if self.__right is None:
                self.__right = Node(v, self)
            else:
                self.__right.add(v)


class BinaryTree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, val):
        self.__root = val

    def add_data(self, data):
        if self.__root == None:
            self.__root = Node(data)
            return

        cn = self.__root
        while 1:
            if data < cn.data:
                if cn.left == None:
                    cn.left = Node(data, parent=cn)
                    return
                else:
                    cn = cn.left
            elif data > cn.data:
                if cn.right == None:
                    cn.right = Node(data, parent=cn)
                    return
                else:
                    cn = cn.right
            else:
                return

    def print_by_level(self):
        current_level_nodes = []
        next_level_nodes = []

        current_level_nodes.append(self.__root)

        while len(current_level_nodes) > 0:
            current_level_data = []
            for node in current_level_nodes:
                current_level_data.append(node.data)
                if node.left is not None:
                    next_level_nodes.append(node.left)
                if node.right is not None:
                    next_level_nodes.append(node.right)

            print(" ".join(str(data) for data in current_level_data))
            current_level_nodes.clear()
            current_level_nodes = [n for n in next_level_nodes]
            next_level_nodes.clear()

    def search(self, el):
        cn = self.__root

        while cn is not None:
            if cn.data == el:
                return cn
            elif el < cn.data:
                cn = cn.left
            else:
                cn = cn.right

    def predecessor(self, node=None):
        if node is None:
            node = self.__root

        node = node.left

        while node is not None and node.right is not None:
            node = node.right

        return node

    def successor(self, node=None):
        if node is None:
            node = self.__root

        node = node.right

        while node is not None and node.right is not None:
            node = node.left

        return node

    def delete(self, node):
        # Case 1: Node is leaf and has no child nodes
        if node.left is None and node.right is None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None

        # Case 2: Node has one child node.
        elif node.left is None and node.right is not None:
            node.data = node.right.data
            node.right = None
        elif node.left is not None and node.right is None:
            node.data = node.left.data
            node.left = None

        # Case 3: Node has both the childs. Replace the node with the predecessor or successor
        # and recursively call delete on it.
        else:
            predecessor = self.predecessor(node)
            node.data = predecessor.data
            self.delete(predecessor)

    def get_height(self, node):
        if node is None:
            return 0

        height_left = self.get_height(node.left)
        height_right = self.get_height(node.right)

        if height_left > height_right:
            return height_left + 1
        else:
            return height_right + 1

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)


    # A full binary tree (sometimes a proper binary tree or 2-tree is a tree in which every node other than the leaves
    # has 2 children. Diagram below
    #                                           N
    #                                          / \
    #                                        N     N
    #                                       / \   / \
    #                                      N  N  N   N
    def is_full(self, node=None):
        if node is None:
            return True

        if node.left is None and node.right is not None:
            return False
        elif node.left is not None and node.right is None:
            return False
        else:
            return self.is_full(node.left) and self.is_full(node.right)

    def is_complete(self, node=None):
        """
        # The following trees are examples of Complete Binary Trees
        #     1
        #   /   \
        #  2     3
        #
        #        1
        #     /    \
        #    2       3
        #   /
        #  4
        #
        #        1
        #     /    \
        #    2      3
        #   /  \    /
        #  4    5  6

        # The following trees are examples of Non-Complete Binary Trees
        #     1
        #       \
        #        3
        #
        #        1
        #     /    \
        #    2       3
        #     \     /  \
        #      4   5    6
        #
        #        1
        #     /    \
        #    2      3
        #          /  \
        #         4    5
        """
        if node is None:
            return True

        if node.left is None and node.right is not None:
            return False
        else:
            condition1 = self.is_complete(node.left) and self.is_complete(node.right)
            h = self.get_height(self.__root)
            n = self.count_nodes(self.__root)

            condition2 = False
            if n == math.pow(2, h) - 1:
                condition2 = True

            return condition1 and condition2

    def min(self):
        cn = self.__root
        min_v = None
        while cn is not None:
            min_v = cn.data
            cn = cn.left

        return min_v

    def max(self):
        cn = self.__root
        max_v = None
        while cn is not None:
            max_v = cn.data
            cn = cn.right

        return max_v



# Create an artificial dataset for the test case

#                              +-------+
#                              |   3   |
#                              |       |
#                              +-------+
#                              |       |
#                              |       |
#                +-------+-----+       +-----+-------+
#                |   2   |                   |   5   |
#                |       |                   |       |
#                +-------+                   +-------+
#                |       |
#                |       |
# +-------+------+       +-------+--------+
# |   1   |                      |   4    |
# |       |                      |        |
# +-------+                      +--------+

def create_artificial_tree():
    root = Node(3)
    left = Node(2, root)
    right = Node(5, root)

    left_left = Node(1, left)
    left_right = Node(4, left)

    root.left = left
    root.right = right

    left.left = left_left
    left.right = left_right

    return root


def create_tree(*args):
    root = Node(args[0])

    cn = root
    for i in range(1, len(args)):
        v = args[i]
        cn.add(v)

    return root
