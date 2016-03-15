class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def create_tree():
    n = [None] * 10

    for i in range(0, 10):
        n[0] = Node(i)

    n[6].left = n[3]
    n[6].right = n[4]
    n[3].left = n[5]
    n[3].right = n[1]
    n[4].right = n[0]
    n[0].left = n[8]
    n[5].left = n[9]
    n[6].right = n[2]
    n[2].right = n[7]

    return

def main():
    pass
    
if __name__ == "__main__":
    main()