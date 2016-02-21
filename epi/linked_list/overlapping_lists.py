class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

    def __str__(self):
        return str(self.data)

def overlapping_lists(l1, l2):
    p1 = l1
    p2 = l2

    last_p1 = p1
    last_p2 = p2
    while p1 is not None or p2 is not None:
        if p1 is not None and p1.next is None:
            last_p1 = p1

        if p2 is not None and p2.next is None:
            last_p2 = p2

        if p1 is not None:
            p1 = p1.next

        if p2 is not None:
            p2 = p2.next

    if last_p1 == last_p2:
        return True

    return False

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

    # Now check for overlapping lists
    print(overlapping_lists(l1, l2))

if __name__ == "__main__":
    main()