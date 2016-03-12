from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

    __repr__ = __str__

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if self.root == None:
            self.root = Node(data)
            return

        if node == None:
            node = Node(data)
            return node

        if data < node.data:
            if node.left is None:
                node.left = self.insert(node.left, data)
                node.left.parent = node
            else:
                self.insert(node.left, data)

        elif data > node.data:
            if node.right is None:
                node.right = self.insert(node.right, data)
                node.right.parent = node
            else:
                self.insert(node.right, data)

    def find_node(self, data):
        curr = self.root
        parent = None
        while curr is not None:
            parent = curr
            if data == curr.data:
                return curr
            elif data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        if parent.data == data:
            return parent

        return None

    def find_lowest_leaf_node(self):
        curr = self.root
        while curr.right is not None:
            curr = curr.right

        # Now we have the right most element. Now find the element
        while True:
            if curr.right is not None:
                curr = curr.right
            elif curr.left is not None:
                curr = curr.left
            else:
                break

        return curr

    def sort(self, node, sorted_els):
        if node is None:
            return sorted_els

        if node.left == None and node.right == None:
            # We have come to a leaf node
            sorted_els.append(node)
            return sorted_els

        sorted_els = self.sort(node.left, sorted_els)
        sorted_els.append(node)
        sorted_els = self.sort(node.right, sorted_els)

        return sorted_els

    def dfs_sum(self, node):
        sum = 0

        if node is None:
            return 0

        sum += self.dfs_sum(node.left)
        sum += self.dfs_sum(node.right)
        sum += node.data

        return sum

    def max_sum(self, node):
        sum_right = self.dfs_sum(node.right)

        sum_parent = 0
        if node.parent is not None and node.parent.left == node:
            node.parent.left = None
            sum_parent = self.dfs_sum(node.parent)
            node.parent.left = node

        return sum_right + sum_parent

def create_bst():
    bst = BST()
    arr = [11, 2, 29, 1, 7, 15, 40, 35]

    for el in arr:
        bst.insert(bst.root, el)

    return bst

def main():
    bst = create_bst()
    # sorted_els = []
    # sorted_els = bst.sort(bst.root, sorted_els)
    # print(sorted_els)
    # new_sorted_els = [node.data for node in sorted_els]
    # new_sorted_els[-2] = new_sorted_els[-1]
    # for i in range((len(sorted_els) - 1) - 2, 0, -1):
    #     sorted_els[i].data = sorted_els[i+1].data + new_sorted_els[i+1]
    #     new_sorted_els[i+1] = sorted_els[i+1].data
    #
    # new_sorted_els[-2] = sorted_els[-1].data
    # print(sorted_els)

    print(bst.max_sum(node))

    
if __name__ == "__main__":
    main()