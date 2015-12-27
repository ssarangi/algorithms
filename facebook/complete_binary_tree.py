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
            return self.is_complete(node.left) and self.is_complete(node.right)

def main():
    binary_tree = BinaryTree()
    input = [17, 5, 35, 2, 16, 29, 38, 33, 19, 36, 40]

    print("Print by Level:")
    for i in input:
        binary_tree.add_data(i)

    binary_tree.print_by_level()

    print("Search Result:")
    node = binary_tree.search(16)
    if node is not None:
        print(node)

    print("Predecessor:")
    predecessor = binary_tree.predecessor(binary_tree.root)
    print(predecessor)

    print("Successor:")
    successor = binary_tree.successor(binary_tree.root)
    print(successor)

    print("Deleting Node 29:")
    node = binary_tree.search(36)
    binary_tree.delete(node)
    binary_tree.print_by_level()

    print("Is Tree Full:")
    print(binary_tree.is_full(binary_tree.root))

    print("Is Tree Complete:")
    print(binary_tree.is_complete(binary_tree.root))

if __name__ == "__main__":
    main()
