class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def add(self, v):
        if self.root is None:
            self.root = Node(v)
        else:
            cn = self.root
            prev = cn
            while cn is not None:
                prev = cn
                if cn.data > v:
                    cn = cn.left
                else:
                    cn = cn.right

            if v < prev.data:
                prev.left = Node(v)
            else:
                prev.right = Node(v)

    def valid(self, node):
        if node is None:
            return True

        if (node.left is not None and node.left.data > node.data) or \
           (node.right is not None and node.right.data < node.data):
           return False

        return self.valid(node.left) and self.valid(node.right)


def main():
    a1 = [19, 7, 43, 3, 11, 2, 5, 17, 13, 23, 47, 37, 53, 29, 41, 31]

    bst = BST()
    for elm in a1:
        bst.add(elm)

    print(bst.valid(bst.root))

if __name__ == "__main__":
    main()