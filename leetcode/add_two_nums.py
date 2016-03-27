class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None

def create_list(arr):
    head = None
    cn = None
    prev = None
    for el in arr:
        cn = ListNode(el)
        if head is None:
            head = cn
        
        if prev is not None:            
            prev.next = cn
        
        prev = cn
        
    return head

def reverse_list(l):
    cn = l
    next = cn.next
    cn.next = None
    
    if next is None:
        return l
    
    while cn is not None and next is not None:
        tmp = next.next
        next.next = cn
        cn = next
        next = tmp
        
    return cn
        
def print_ll(l1):
    cn = l1
    arr = []
    while cn is not None:
        arr.append(cn.val)
        cn = cn.next
    
    arr = [str(num) for num in arr]
    print(" -> ".join(arr))

def add_two_numbers(l1, l2):
    cn1 = l1
    cn2 = l2
    head = None
    cn = None
    prev = None
    
    carryover = 0
    while cn1 is not None or cn2 is not None or carryover > 0:
        d1 = 0
        d2 = 0
        n1next = None
        n2next = None
        
        if cn1 is not None:
            d1 = cn1.val
            n1next = cn1.next
            
        if cn2 is not None:
            d2 = cn2.val
            n2next = cn2.next
        
        sum = d1 + d2 + carryover
        carryover = sum // 10
        v = sum % 10
        cn = ListNode(v)
        
        if head is None:
            head = cn
            
        if prev is not None:
            prev.next = cn
            
        prev = cn
        
        cn1 = n1next
        cn2 = n2next
        
    return head

# n1 = create_list([2, 4, 3])
# n2 = create_list([5, 6, 4])
n1 = create_list([5])
n2 = create_list([5])

result = add_two_numbers(n1, n2)
print_ll(result)