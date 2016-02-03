"""
The MIT License (MIT)

Copyright (c) 2015 <Satyajit Sarangi>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

class Node:
    def __init__(self, id, next=None):
        self.id = id
        self.next = next

    def __str__(self):
        return str(self.id)

def create_linked_list_from_list(ll):
    head = None
    prev_node = None
    for el in ll:
        node = Node(el)
        if head is None:
            head = node
            prev_node = head

        prev_node.next = node
        prev_node = node

    return head

def traverse_list(head):
    # Return 2 nodes. One which is the last node and the node before it
    last_node = head
    last_but_one_node = None


    while last_node.next is not None:
        last_but_one_node = last_node
        last_node = last_node.next

    return last_node, last_but_one_node

def zip_list(head):
    start_node = head

    while start_node is not None:
        last_node, last_but_one_node = traverse_list(start_node)
        # Realign the pointers
        last_but_one_node.next = None
        curr_next_node = start_node.next
        start_node.next = last_node
        last_node.next = curr_next_node

        # Change the start node
        start_node = curr_next_node


def find_length(head):
    length = 0
    node = head
    while node is not None:
        node = node.next
        length += 1

    return length

def find_mid_pt(head):
    length = find_length(head)
    assert length % 2 == 0
    mid_pt = length // 2

    current = 0
    mid_pt_node = None
    mid_pt_minus_one_node = None
    node = head

    while node.next is not None:
        if current == mid_pt:
            mid_pt_node = node

        if current == mid_pt - 1:
            mid_pt_minus_one_node = node

        current += 1
        node = node.next

    return mid_pt_node, mid_pt_minus_one_node, node

def reverse_linked_list(head):
    node = head
    node_next = node.next
    last_node = None

    while node is not None:
        last_node = node

        if node_next is not None:
            node_next_next = node_next.next
            node_next.next = node

        node = node_next

        if node_next is not None:
            node_next = node_next_next

    head.next = None
    return last_node

def zip_list_linear_time(head):
    mid_pt, mid_pt_minus_one, last_node = find_mid_pt(head)

    mid_pt_minus_one.next = None
    end_head = reverse_linked_list(mid_pt)

    node = head
    end_pt = end_head

    while end_pt is not None:
        node_next = node.next
        end_pt_next = end_pt.next
        node.next = end_pt
        node.next.next = node_next
        node = node_next
        end_pt = end_pt_next

def print_linked_list(head):
    node = head
    while node is not None:
        print(node.id)
        node = node.next

def main():
    head = create_linked_list_from_list([1,2,3,4,5,6])
    # zip_list(head)
    zip_list_linear_time(head)
    print_linked_list(head)

if __name__ == "__main__":
    main()