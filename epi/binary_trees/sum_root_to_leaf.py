class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def sum_root_to_leaf(root):
    pass

def create_tree():
    A = Node(1)
    B = Node(0)
    C = Node(0)
    D = Node(0)
    E = Node(1)
    F = Node(1)
    G = Node(1)
    H = Node(0)
    I = Node(1)
    J = Node(0)
    O = Node(0)
    K = Node(0)
    L = Node(1)
    M = Node(1)
    N = Node(0)
    O = Node(0)
    P = Node(0)

    A.left = B
    A.right = I
    B.left = C
    B.right = F
    C.left = D
    C.right = E
    F.right = G
    G.left = H
    I.left = J
    I.right = O
    O.right = P
    J.right = K
    K.left = L
    K.right = N
    L.right = M

    return A

def main():
    root = create_tree()

    
if __name__ == "__main__":
    main()