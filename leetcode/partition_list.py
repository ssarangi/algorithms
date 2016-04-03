# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head):
    cn = head
    
    while cn is not None:
        print(cn.val, end = " ")
        cn = cn.next
        
    print("")
    
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
            
        l1 = None
        l2 = None
        
        cn = head
        new_head_l1 = None
        new_head_l2 = None
        prev_l1 = head

        while cn is not None:
            # New Node creation
            nn = ListNode(cn.val)
            if cn.val >= x:
                if l2 is None:
                    l2 = nn
                    new_head_l2 = nn
                else:
                    l2.next = nn
                    l2 = l2.next
            else:
                if l1 is None:
                    l1 = nn
                    new_head_l1 = nn
                else:
                    l1.next = nn
                    prev_l1 = nn
                    l1 = l1.next
                    
            cn = cn.next

        prev_l1.next = new_head_l2
        
        if new_head_l1 is None and new_head_l2 is not None:
            return new_head_l2
            
        return new_head_l1

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
    
soln = Solution()

l = create_list(1, 4, 3, 2, 5, 2)
l = create_list(1, 2)
print_list(soln.partition(l, 2))
