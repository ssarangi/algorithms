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
                prev.left.parent = prev
            else:
                prev.right = Node(v)
                prev.right.parent = prev

    def valid(self, node):
        if node is None:
            return True

        if (node.left is not None and node.left.data > node.data) or \
           (node.right is not None and node.right.data < node.data):
           return False

        return self.valid(node.left) and self.valid(node.right)

    def find_key(self, k):
        cn = self.root
        while cn is not None and cn.data != k:
            if k > cn.data:
                cn = cn.right
            else:
                cn = cn.left

        return cn

    def find_next_largest_element(self, k):
        start_node = self.find_key(k)
        if start_node is None:
            return None

        # Find the parent which has a right child
        parent = start_node.parent
        level = 1
        while parent.right is None or parent.right == start_node:
            parent = parent.parent
            level += 1

        # Now we found the parent
        # So drill down to the exact level and get the next element
        next_el = parent.right
        node = next_el
        prev = node

        while node is not None and level > 0:
            prev = node
            if node.left is not None:
                node = node.left
            else:
                node = node.right
            level -= 1

        return prev

class Stack(list):
    def push(self, el):
        self.append(el)

    def empty(self):
        return len(self) == 0

    def top(self):
        if len(self) > 0:
            return self[-1]

        raise Exception("Top called on an empty stack")

def sorted_order(node):
    s = Stack()
    curr = node

    result = []
    while not s.empty() or curr:
        if curr:
            s.push(curr)
            curr = curr.left
        else:
            curr = s.top()
            s.pop()
            result.append(curr.data)
            curr = curr.right

    return result

def main():
    a1 = [19, 7, 43, 3, 11, 2, 5, 17, 13, 23, 47, 37, 53, 29, 41, 31]

    bst = BST()
    for elm in a1:
        bst.add(elm)

    node = bst.find_key(43)
    print(sorted_order(node))

if __name__ == "__main__":
    main()