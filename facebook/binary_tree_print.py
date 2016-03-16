class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)

    __repr__ = __str__

#            6
#           / \
#          3   4
#         / \   \
#        5   1   0
#       / \     /
#      9   2   8
#           \
#            7
#
#  ============>
#  9 5 3 2 6 1 7 4 8 0

def create_tree():
    n = [None] * 10

    for i in range(0, 10):
        n[i] = Node(i)

    n[6].left = n[3]
    n[6].right = n[4]
    n[3].left = n[5]
    n[3].right = n[1]
    n[4].right = n[0]
    n[0].left = n[8]
    n[5].left = n[9]
    n[5].right = n[2]
    n[2].right = n[7]

    return n[6]

def column_printer(tree):
    node_by_column = {}

    min_column = 0
    max_column = 0

    traverse_stack = [(tree, 0)]

    while len(traverse_stack) > 0:

        node, column = traverse_stack.pop()

        if column not in node_by_column:
            node_by_column[column] = []

        node_by_column[column].append(node)

        for n, d in [(node.left, -1), (node.right, 1)]:
            if n is not None:
                traverse_stack.append((n, column + d))
                min_column = min(column + d, min_column)
                max_column = max(column + d, max_column)

    result = []

    for i in range(min_column, max_column + 1):
        result += [str(x.data) for x in node_by_column[i]]

    print(",".join(result))

def main():
    root = create_tree()
    # arr = []
    # print_column_wise(root, arr)
    column_printer(root)
    
if __name__ == "__main__":
    main()