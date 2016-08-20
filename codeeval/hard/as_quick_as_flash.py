import sys

def partition(numbers, start, end, pivots):
    pivot_el = numbers[start + (end - start) // 2]
    pivot_idx = start + (end - start) // 2
    
    i = start
    j = end
    terminate = False
    while not terminate:
        while i <= j and numbers[i] < pivot_el:
            i += 1
            
        while i <= j and numbers[j] > pivot_el:
            j -= 1
            
        if j < i:
            terminate = True
        else:
            numbers[i], numbers[j] = numbers[i], numbers[j]
            
    return pivot_idx

def quicksort(numbers, start, end, pivots):
    if start < end:
        pivot = partition(numbers, start, end, pivots)
        
        quicksort(numbers, start, pivot - 1, pivots)
        quicksort(numbers, pivot + 1, end, pivots)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        numbers = [int(d) for d in test.split(" ")]
        pivots = []
        print(numbers)
        quicksort(numbers, 0, len(numbers) - 1, pivots)
        print(numbers)
        print(len(pivots))