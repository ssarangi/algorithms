from queue import Queue

class Node:
    def __init__(self, data=None):
        self._left = None
        self._right = None
        self.parent = None
        self.data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, l):
        self._left = l
        l.parent = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, r):
        self._right = r
        r.parent = self

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return str(self.data)

    __repr__ = __str__

def create_tree():
    root = Node(314)
    root.left = Node(6)
    root.right = Node(6)

    left = root.left
    right = root.right

    left.right = Node(2)
    left.right.right = Node(3)

    right.left = Node(2)
    right.left.left = Node(3)

    return root

def is_arr_symmetric(arr):
    if len(arr) == 1:
        return True

    if len(arr) % 2 != 0:
        return False

    p1 = 0
    p2 = len(arr) - 1
    while p2 > p1:
        if arr[p1] != arr[p2]:
            return False

        p1 += 1
        p2 -= 1

    return True

# Traverse the left subtree and make sure the right one has the same one in flipped order
def test_symmetric(root):
    q = Queue()
    q.put((root, 0))

    level = 0
    nodes_at_current_level = []
    while not q.empty():
        node, current_level = q.get()
        if current_level != level:
            if not is_arr_symmetric(nodes_at_current_level):
                return False

            # Clear the array now
            nodes_at_current_level.clear()
            level = current_level

        nodes_at_current_level.append(node)

        if node.left is not None:
            q.put((node.left, current_level + 1))

        if node.right is not None:
            q.put((node.right, current_level + 1))

    # Check the last level here
    return is_arr_symmetric(nodes_at_current_level)

def main():
    root = create_tree()
    print(test_symmetric(root))
    
if __name__ == "__main__":
    main()