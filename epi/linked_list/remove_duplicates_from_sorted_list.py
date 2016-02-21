# TODO: NOT COMPLETE
class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

    def __str__(self):
        return str(self.data)

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

def find_middle(head):
    slow_ptr = head
    fast_ptr = head

    if head is not None:
        while fast_ptr is not None and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

    return slow_ptr

def sort_list(l):
    cn = l
    while cn is not None:
        print(cn, end=' ')
        cn = cn.next

    print("")

def merge(l1, l2):
    cn1 = l1
    cn2 = l2

    if cn1.data > cn2.data:
        output = cn2
        cn2 = cn2.next
    else:
        output = cn1
        cn1 = cn1.next

    while cn1 is not None or cn2 is not None:
        if cn1.data > cn2.data:
            output.next = cn2
            cn2 = cn2.next
        else:
            output.next = cn1
            cn1 = cn1.next

    return output


def merge_sort(l):
    if l.next is None or l.next.next is None:
        if l.next is not None and l.data > l.next.data:
            l.data, l.next.data = l.next.data, l.data

        return l

    middle = find_middle(l)
    middle_next = middle.next
    middle.next = None
    l1 = merge_sort(l)
    l2 = merge_sort(middle_next)

    output = merge(l1, l2)
    return output


def main():
    l = create_list(9, 4, 7, 2, 6, 4, 2, 0, 1, 3, 6, 7)
    l = create_list(5, 4, 3, 2)
    print(find_middle(l))
    merge_sort(l)
    
if __name__ == "__main__":
    main()