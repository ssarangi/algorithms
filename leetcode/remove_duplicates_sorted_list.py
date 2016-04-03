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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        elements = {}
        cn = head
        
        prev = None
        while cn is not None:
            if cn.val not in elements:
                elements[cn.val] = True
                prev = cn
                cn = cn.next
            else:
                # Head node cannot be deleted since no other elements
                # have been added to it yet.
                # This is the last node
                if cn.next is None:
                    prev.next = None
                    prev = cn
                    cn = cn.next
                else:
                    cn.val = cn.next.val
                    cn.next = cn.next.next

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
    
soln = Solution()

l = create_list(1, 1, 1)
print_list(soln.deleteDuplicates(l))
