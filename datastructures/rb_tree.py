"""
The MIT License (MIT)

Copyright (c) 2015 <Satyajit Sarangi>

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

"""
Red Black Trees
"""

class NullNode:
    def __init__(self):
        self._color = RBTreeNode.BLACK

    @property
    def color(self):
        return self._color

    def __str__(self):
        return "NullNode"

    __repr__ = __str__

class RBTreeNode:
    BLACK = 'black'
    RED   = 'red'

    def __init__(self, data, color):
        self._color = color
        self._data = data
        self._left = NullNode()
        self._right = NullNode()
        self._parent = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, c):
        self._color = c

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, v):
        self._left = v

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, v):
        self._right = v

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, v):
        self._data = v

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, p):
        self._parent = p

    def __str__(self):
        return str(self.data) + "::" + self._color

    __repr__ = __str__

class RBTree:
    def __init__(self):
        self._root = None

    def _insert(self, data, node):
        if isinstance(node, NullNode):
            return RBTreeNode(data, RBTreeNode.RED)

        inserted_node = None
        if data < node.data:
            inserted_node = self._insert(data, node.left)
            if isinstance(node.left, NullNode):
                node.left = inserted_node
                node.left.parent = node
        else:
            inserted_node = self._insert(data, node.right)
            if isinstance(node.right, NullNode):
                node.right = inserted_node
                node.right.parent = node

        return inserted_node

    def rotate_right(self, node):
        #                   node                     P
        #                 /      \                 /   \
        #                P        C      -->      A    node
        #               / \                           /    \
        #              A   B                         B      C

        left_child = node.left

        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = left_child
            else:
                node.parent.right = left_child

        node.left = left_child.right
        left_child.parent = node.parent
        left_child.right = node
        node.parent = left_child

        if node == self._root:
            self._root = left_child


    def rotate_left(self, node):
        #                   node                     P
        #                 /      \                 /   \
        #                P        C      <--      A    node
        #               / \                           /    \
        #              A   B                         B      C

        right_child = node.right

        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = right_child
            else:
                node.parent.right = right_child

        node.right = right_child.left
        right_child.parent = node.parent
        right_child.left = node
        node.parent = right_child

        if node == self._root:
            self._root = right_child

    def insert(self, data):
        inserted_node = None
        if self._root is None:
            self._root = RBTreeNode(data, RBTreeNode.BLACK)
            inserted_node = self._root
        else:
            inserted_node = self._insert(data, self._root)

        # Check if the parent of current node is not Black or x is root
        while inserted_node != self._root and inserted_node.parent.color != RBTreeNode.BLACK:
            # If inserted_node's uncle is red
            grand_parent = inserted_node.parent.parent
            parent = inserted_node.parent

            if parent == grand_parent.left:
                uncle = grand_parent.right
            else:
                uncle = grand_parent.left

            if uncle.color == RBTreeNode.RED:
                if not isinstance(uncle, NullNode):
                    uncle.color        = RBTreeNode.BLACK

                parent.color       = RBTreeNode.BLACK
                grand_parent.color = RBTreeNode.RED
                inserted_node = grand_parent
            elif uncle.color == RBTreeNode.BLACK:
                x = inserted_node

                if parent == grand_parent.left and x == parent.left:
                    # Left Left Case
                    #                    G                                    P
                    #                  /   \                                /   \
                    #                 P     U                              x     G
                    #               /  \   / \          ------->          / \   /  \
                    #              x   T3 T4 T5                          T1 T2 T3   U
                    #             / \                                              / \
                    #            T1 T2                                            T4 T5
                    self.rotate_right(grand_parent)
                elif parent == grand_parent.left and x == parent.right:
                    # Right Left Case
                    #                    G                                    P
                    #                  /   \                                /   \
                    #                 P     U                              x     G
                    #               /  \   / \          ------->          / \   / \
                    #              T1  x  T4 T5                          T1 T2 T3  U
                    #                 / \                                         / \
                    #                T2 T3                                       T4 T5
                    self.rotate_left(parent)
                    self.rotate_right(grand_parent)
                elif parent == grand_parent.right and x == parent.right:
                    # Right Right case
                    self.rotate_left(grand_parent)
                elif parent == grand_parent.right and x == parent.left:
                    # Left Right case
                    self.rotate_right(parent)
                    self.rotate_left(grand_parent)

                grand_parent.color, parent.color = parent.color, grand_parent.color

        self._root.color = RBTreeNode.BLACK

    def search(self, data, node=None):
        if node == None:
            node = self._root

        if node == None or isinstance(node, NullNode):
            return None

        if data < node.data:
            return self.search(node.left)
        else:
            return self.search(node.right)


    def find_predecessor(self, node):
        if isinstance(node.right, NullNode):
            return node
        else:
            return self.find_predecessor(node.right)

    def find_successor(self, node):
        if isinstance(node.left, NullNode):
            return node
        else:
            return self.find_successor(node.left)

    def delete(self, data):
        node = self.search(data)
        if node == None:
            return




def main():
    rbtree = RBTree()
    # arr = [10,20,30,15]
    arr = [3, 7, 10, 8, 11, 22, 26, 18, 2, 7, 13]
    for item in arr:
        rbtree.insert(item)

if __name__ == "__main__":
    main()