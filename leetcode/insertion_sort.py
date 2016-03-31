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
    def __init__(self):
        self.head = None
        
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        while head is not None:
            node = ListNode(head.val)

            if self.head is None:
                self.head = node
            # Check if the head is less than the current list head we have
            elif node.val <= self.head.val:
                tmp = self.head
                self.head = node
                self.head.next = tmp
            else:
                cn = self.head
                prev = None
                while cn is not None and cn.val < node.val:
                    prev = cn
                    cn = cn.next

                prev.next = node
                node.next = cn

            head = head.next
            
        return self.head
    
soln = Solution()

head = create_list(4,2,7,1,9,3,10,20,11,14)
head = create_list(1, 1)
new_head = soln.insertionSortList(head)
print_list(new_head)