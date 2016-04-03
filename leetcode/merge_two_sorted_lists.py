# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        
        # Output Node
        on = None
        head = None
        
        if l1 is None and l2 is not None:
            head = l2
        elif l1 is not None and l2 is None:
            head = l1
        
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                # Store the value of p1 next
                p1nxt = p1.next
                
                # Arrange p1 -> p2
                p1.next = p2
                cn = p1
                p1 = p1nxt
            else:
                # Store the value of p2 next
                p2nxt = p2.next
                
                # Arrange p2 -> p1
                p2.next = p1
                cn = p2
                
                p2 = p2nxt
            
            if on is not None:
                on.next = cn
            else:
                head = cn
                
            on = cn
            
        return head

def create_list(*args):
    head = None
    prev = None
    for el in args:
        cn = ListNode(el)
        
        if head is None:
            head = cn
            
        if prev is not None:
            prev.next = cn
        
        prev = cn
        
    return head
    
def print_list(head):
    cn = head
    
    while cn is not None:
        print(cn.val, end = " ")
        cn = cn.next
    
soln = Solution()

# l1 = create_list(1, 3, 5, 7, 9)
# l2 = create_list(2, 4, 6, 8, 10, 12, 14, 16, 18)

l1 = create_list(1)
l2 = create_list(2)
print_list(soln.mergeTwoLists(l1, l2))
