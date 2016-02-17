class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, v):
        cn = self.root
        prev = cn
        while cn is not None:
            prev = cn
            if v < cn.data:
                cn = cn.left
            else:
                cn = cn.right

        cn = Node(v)
        if prev.data > v:
            prev.left = cn
        else:
            prev.right = cn

    def get_height(self, node, height):

        height_l = 0
        height_r = 0
        if node.left is not None:
            height_l = self.get_height(node.left, height + 1)

        if node.right is not None:
            height_r = self.get_height(node.right, height + 1)

        max_h = max(height_l, height_r)
        height += max_h
        return height

    def is_balanced(self):
        height_left = 0
        height_right = 0

        if self.root.left is not None:
            height_left = self.get_height(self.root.left, 1)

        if self.root.right is not None:
            height_right = self.get_height(self.root.right, 1)

        if abs(height_right - height_left) > 1:
            return False

        return True

def create_tree():
    bin_tree = BinaryTree()
    bin_tree.root = Node(1)

    arr = [4,2,6,8,3,5,0,9,10,15,12,11]

    for elm in arr:
        bin_tree.add(elm)

    print(bin_tree.is_balanced())

def main():
    create_tree()

if __name__ == "__main__":
    main()
