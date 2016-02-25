class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

    def __str__(self):
        return str(self.data)

def k_cyclic_shift(head, k):
    cn = head
    counter = 0
    kth_ptr = None
    prev = None
    while cn is not None:
        if kth_ptr is not None:
            kth_ptr = kth_ptr.next

        counter += 1
        if k + 1 == counter:
            kth_ptr = head

        prev = cn
        cn = cn.next

    # Prev has the last element.
    prev.next = head
    head = kth_ptr.next
    kth_ptr.next = None
    return head

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


def print_list(head):
    cn = head
    while cn is not None:
        print(cn.data, end=" ")
        cn = cn.next

def main():
    l1 = create_list(1, 2, 3, 4, 5)
    l1 = k_cyclic_shift(l1, k=3)
    print_list(l1)
    
if __name__ == "__main__":
    main()