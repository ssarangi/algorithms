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

# LINK: http://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
from geeksforgeeks.bst.bst import Node, create_artificial_tree

def check_if_bst(node, ancestor_val=None):
    """
    Checks if a given node is a BST or not. To check this we have to check multiple things
    1) The left subtree of a node contains only nodes which are less than the node's keys
    2) The right subtree of a node contains only nodes which are greater than the node's keys
    3) Both the left and right subtrees are also BST's
    :param node: Current node being checked
    :param ancestor_val: The ancestor's value which needs to be checked
    :return: Bool
    """
    if node is None:
        return True

    if node.left is not None:
        if node.data < node.left.data:
            return False

        if ancestor_val is not None and node.parent.right == node and node.left.data < ancestor_val:
            return False

    if node.right is not None:
        if node.data > node.right.data:
            return False

        if ancestor_val is not None and node.parent.left == node and node.right.data > ancestor_val:
            return False

    return check_if_bst(node.left, node.data) and check_if_bst(node.right, node.data)

def main():
    root = create_artificial_tree()
    print(check_if_bst(root))

if __name__ == "__main__":
    main()