import sys
import heapq

def nth_element(n, k, a, b, c, r):
    m = [0] * n
    m[0] = a
    max_available_els = max(a, b, c, r)
    minheap_availablenums = [i for i in range(0, max_available_els + 1)]
    minheap_availablenums.remove(a)
    
    for i in range(1, k):
        m[i] = (b * m[i-1] + c) % r
        
        if m[i] in minheap_availablenums:
            minheap_availablenums.remove(m[i])

    for i in range(k, n):
        if i > k:
            # Add the k-1th element to the heap of available elements
            v = m[i - k - 1]
            heapq.heappush(minheap_availablenums, v)
            
        smallest_v = heapq.heappop(minheap_availablenums)
        m[i] = smallest_v

    return m[n-1]

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        n,k,a,b,c,r = [int(v) for v in test.split(",")]
        nth_el = nth_element(n, k, a, b, c, r)
        print(nth_el)