class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

def create_linked_list(*args):
    current_node = None
    prev_node = None
    head = None
    for arg in args:
        node = Node(arg)

        if current_node is None:
            head = node

        current_node = node

        if prev_node is not None:
            prev_node.next = current_node
            prev_node = current_node

        prev_node = current_node

    return head

def merge_sorted_list(l1, l2):
    prev_ptr_l1 = None
    ptr_l1 = l1

    ptr_l2 = l2

    while ptr_l1 is not None and ptr_l2 is not None:
        if ptr_l1.val <= ptr_l2.val:
            prev_ptr_l1 = ptr_l1
            ptr_l1 = ptr_l1.next
        elif ptr_l1.val > ptr_l2.val:
            # So insert it in between the prev one and this one
            new_node = Node(ptr_l2.val, ptr_l1)

            if prev_ptr_l1 is None:
                # This means we are at head. So create a new node
                prev_ptr_l1 = new_node
                prev_ptr_l1.next = ptr_l1
                l1 = prev_ptr_l1
                ptr_l1 = l1
                prev_ptr_l1 = None
            else:
                prev_ptr_l1.next = new_node
                prev_ptr_l1.next.next = ptr_l1
                prev_ptr_l1 = new_node

            ptr_l2 = ptr_l2.next

    return l1

def ll_to_str(l):
    s = ""
    while l is not None:
        s += str(l.val) + " "
        l = l.next

    return s

def test_case(l1, l2):
    l3 = merge_sorted_list(l1, l2)
    print(ll_to_str(l3))


def main():
    l1 = create_linked_list(1, 3, 5, 7, 9)
    l2 = create_linked_list(2, 4, 6, 8, 10)

    test_case(l1, l2)

    l1 = create_linked_list(10, 12, 14)
    l2 = create_linked_list(1, 2, 3)

    test_case(l1, l2)

    l1 = create_linked_list(1, 3, 5, 7, 9)
    l2 = create_linked_list(12, 14, 16, 18)

    test_case(l1, l2)


if __name__ == "__main__":
    main()