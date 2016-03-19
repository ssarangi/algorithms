# Merge k sorted singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_list(*arr):
    arr = sorted(arr)
    prev = None
    head = None
    for el in arr:
        node = Node(el)
        if head is None:
            head = node

        if prev is not None:
            prev.next = node

        prev = node

    return head

import sys

def merge_k_sorted_list(*args):
    list_heads = [arg for arg in args]

    new_head = None
    cn = None

    while len(list_heads) > 0:
        min_node = list_heads[0]
        min_node_idx = 0

        for i, node in enumerate(list_heads):
            if node.data < min_node.data:
                min_node_idx = i
                min_node = node

        if new_head is None:
            new_head = Node(min_node.data)

        if cn is None:
            cn = new_head
        else:
            cn.next = Node(min_node.data)
            cn = cn.next

        if min_node.next is not None:
            list_heads[min_node_idx] = min_node.next
        else:
            list_heads.remove(min_node)

    return new_head


def print_list(head):
    cn = head
    while cn is not None:
        print(cn.data, end=", ")
        cn = cn.next

l1 = create_list(1, 3, 5, 7, 11, 15)
l2 = create_list(4, 6, 8, 10)
l3 = create_list(2, 9, 12, 13)

new_head = merge_k_sorted_list(l1, l2, l3)
print_list(new_head)
