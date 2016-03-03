class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def create_unbalanced_tree():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)

    one.right = two
    two.right = three
    three.right = five
    five.left = four
    five.right = six

    return one

def balance_tree(root):
    pass

def main():
    root = create_unbalanced_tree()
    root = balance_tree(root)
    print(root)
    
if __name__ == "__main__":
    main()