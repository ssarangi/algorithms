class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

def create_ll(*args):
    head = Node(args[0])

    cn = head
    for el in args[1:]:
        nn = Node(el)
        cn.next = nn
        cn = nn

    return head

def reverse_ll(head):
    cn = head
    prev = None
    while cn is not None:
        if prev is not None:
            actual_next = cn.next
            cn.next = prev
            prev = cn
            cn = actual_next
        else:
            prev = cn
            cn = cn.next
            prev.next = None

    return prev

def print_ll(head):
    cn = head
    s = ""
    while cn is not None:
        s += str(cn.val) + " "
        cn = cn.next

    print(s)

def main():
    l1 = create_ll(1, 2, 3, 4, 5, 6, 7)
    reversed = reverse_ll(l1)
    print_ll(reversed)

if __name__ == "__main__":
    main()