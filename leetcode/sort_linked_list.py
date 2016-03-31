# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head):
    cn = head
    while cn is not None:
        print(cn.val, end=" ")
        cn = cn.next

def create_list(*args):
    head = None
    cn = None
    prev = None
    for arg in args:
        cn = ListNode(arg)
        if head is None:
            head = cn
            
        if prev is not None:
            prev.next = cn
            
        prev = cn
        
    return head
    
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def splitList(head):
            pass
        
        if head is None or head.next is None:
            return head
            
        
    
soln = Solution()

head = create_list(4,2,7,1,9,3,10,20,11,14)
head = create_list(1, 1)
new_head = soln.sortList(head)
print_list(new_head)