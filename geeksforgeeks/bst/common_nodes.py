"""
http://www.geeksforgeeks.org/print-common-nodes-in-two-binary-search-trees/
Given two Binary Search Trees, find common nodes in them. In other words, find intersection of two BSTs.
"""

from geeksforgeeks.bst.bst import Node, create_tree

def common_nodes(t1, t2):
    pass

def main():
    t1 = create_tree(5, 1, 10, 0, 4, 7, 9)
    t2 = create_tree(10, 7, 20, 4, 9)

    print(common_nodes(t1, t2))

if __name__ == "__main__":
    main()