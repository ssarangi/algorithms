from balanced_binary_tree import Node, BinaryTree, create_tree

def find_lca(node1, node2):
    if node1 is None or node2 is None:
        return None

    if node1 == node2:
        return node1

    p1 = node1.parent
    p2 = node2.parent

    visited = {}
    while p1 is not None or p2 is not None:
        if p1 == p2:
            return p1

        if p1 is not None and p1 in visited:
            return p1

        if p2 is not None and p2 in visited:
            return p2

        if p1 is not None:
            visited[p1] = True
            p1 = p1.parent

        if p2 is not None:
            visited[p2] = True
            p2 = p2.parent


    return None

def main():
    tree = create_tree()
    node1 = tree.find(3)
    node2 = tree.find(9)
    lca = find_lca(node1, node2)
    print(lca)

if __name__ == "__main__":
    main()
