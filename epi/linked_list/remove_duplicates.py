class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

    def __str__(self):
        return str(self.data)


# O(n^2) algorithm is simple. Use hash table to do it
def remove_duplicates(head):
    seen = set()
    cn = head
    prev = None
    while cn is not None:
        if cn.data in seen:
            prev.next = cn.next
        else:
            seen.add(cn.data)
            prev = cn

        cn = cn.next

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
    l1 = create_list(1, 2, 3, 4, 5, 3, 2, 1)
    remove_duplicates(l1)
    print_list(l1)


if __name__ == "__main__":
    main()