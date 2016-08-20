def quicksort(arr, start, end):
    pivot = arr[start + (end - start) // 2]
    pivot_el = start + (end - start) // 2
    i = start
    j = end
    
    while i <= j:
        while arr[i] < pivot:
            i += 1
        
        while arr[j] > pivot:
            j -= 1
            
        if (i <= j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    print("arr: %s" % arr)
    print("Pivot: %s" % pivot)
    if start < j:
        print("Sorting: %s" % arr[start: pivot_el])
        quicksort(arr, start, pivot_el)
        
    if i < end:
        print("Sorting: %s" % arr[pivot_el: end])
        quicksort(arr, pivot_el, end)
        
    return arr

import random

arr = [random.randint(0, 20) for _ in range(0, 20)]
# arr = [5, 2, 6, 1, 3, 4]
print("Original: %s" % arr)
print("Sorted: %s" % quicksort(arr, 0, len(arr) - 1))