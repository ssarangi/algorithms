class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

def create_ll(*args):
    nodes_map = {}
    head = Node(args[0])

    cn = head
    for el in args[1:]:
        if el not in nodes_map:
            nn = Node(el)
            nodes_map[el] = nn
        else:
            nn = nodes_map[el]

        cn.next = nn
        cn = nn

    return head

def check_cyclicity(head):
    fast = head
    slow = None

    while slow != fast:
        if fast.next is not None:
            fast = fast.next.next
        else:
            return False

        if slow is None:
            slow = head
        else:
            slow = slow.next

    return True
    
def print_ll(head):
    cn = head
    s = ""
    while cn is not None:
        s += str(cn.val) + " "
        cn = cn.next

    print(s)

def main():
    l1 = create_ll(1, 2, 3, 4, 5, 6, 7, 3)
    cp = check_cyclicity(l1)
    print(cp)
    
if __name__ == "__main__":
    main()