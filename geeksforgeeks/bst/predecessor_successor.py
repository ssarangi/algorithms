class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

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

    def find_successor(self, node):
        if node.right is not None:
            return node.right
        else:
            # Find the ancestor which is the left child of its parent
            parent = node.parent
            while parent is not None:
                if parent.parent.left == parent:
                    return parent.parent
                else:
                    parent = parent.parent

            return None

    def find_predecessor(self, node):
        if node.left is not None:
            curr = node.left
            # Find the rightmost child of the left child
            while curr.right is not None:
                curr = curr.right

            return curr
        else:
            return node.parent

def create_bst():
    bst = BST()
    arr = [8, 3, 5, 0, 1, 9, 13, 2, 4, 10, 15]

    for el in arr:
        bst.insert(bst.root, el)

    return bst

def main():
    bst = create_bst()
    node = bst.find_node(5)
    succ = bst.find_successor(node)
    print(succ)
    node = bst.find_node(13)
    pred = bst.find_predecessor(node)
    print(pred)

if __name__ == "__main__":
    main()