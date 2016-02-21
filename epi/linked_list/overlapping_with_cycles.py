class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

    def __str__(self):
        return str(self.data)

def overlapping_lists(l1, l2):
    pass

def create_list(*args):
    head = None
    prev = None
    for arg in args:
        cn = Node(arg)
        if head is None:
            head = cn

        if prev is not None:
            prev.next = cn

        prev = cn

    return head

def find_end(l):
    prev = None
    cn = l
    while cn is not None:
        prev = cn
        cn = cn.next

    return prev

def main():
    l1 = create_list(1, 2, 3, 4, 5)
    l2 = create_list(6, 7, 8, 9, 0)

    cn = l1
    prev = None
    while cn is not None:
        prev = cn
        cn = cn.next

    n2 = l2.next.next.next
    prev.next = n2

    end2 = find_end(l2)
    end2.next = l2.next

    # Now check for overlapping lists
    print(overlapping_lists(l1, l2))

if __name__ == "__main__":
    main()