class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.jmp = None

    def __str__(self):
        return "(" + str(self.val) + ")"

    def __repr__(self):
        return "(" + str(self.val) + ")"

def create_postings_ll(*args):
    nmap = {}
    v, jmp = args[0]
    head = Node(v)
    nmap[v] = head

    cn = head
    for i in range(1, len(args)):
        v, jmp = args[i]
        nn = Node(v)
        nmap[v] = nn
        cn.next = nn
        cn = nn

    # Now we have the linked list setup. So next thing is to create the jump list
    cn = head
    for v, jmp in args:
        cn.jmp = nmap[jmp]
        cn = cn.next

    return head

def print_ll(head):
    cn = head

    while cn is not None:
        print(cn)
        cn = cn.next

def copy_postings(head):
    cn = head

    head_n = None

    # Pass 1: Create the basic linked list
    prev = None
    while cn is not None:
        if prev is not None:
            prev.next = cn

        cn_n = Node(" = " + str(cn.val))
        if head_n is None:
            head_n = cn_n

        orig_n = cn.next
        cn.next = cn_n
        cn_n.next = orig_n
        cn = orig_n
        prev = cn_n

    cn = head

    # Pass 2: Now fix the jump tables
    while cn is not None:
        cn_n = cn.next
        jmp_to = cn.jmp
        cn_n.jmp = jmp_to.jmp
        cn = cn_n.next

    cn = head

    # Pass 3: Fix the next pointers
    while cn is not None:
        cn_n = cn.next
        cn.next = cn_n.next
        if cn_n.next is not None:
            cn_n.next = cn_n.next.next
        else:
            cn_n.next = None
        cn = cn.next

    return head_n


def main():
    l1 = create_postings_ll(('a', 'c'), ('b', 'd'), ('c', 'b'), ('d', 'd'))
    ch = copy_postings(l1)
    print_ll(ch)

if __name__ == "__main__":
    main()