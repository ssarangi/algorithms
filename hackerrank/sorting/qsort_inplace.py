import sys

def inplace_qsort(arr, start, end):
    pivot = arr[end]
    pivot_idx = end
    end -= 1
    done = False
    while not done:
        while start <= end and arr[start] <= pivot:
            start += 1
        while start <= end and arr[end] >= pivot:
            end -= 1

        if end < start:
            done = True
        else:
            arr[start], arr[end] = arr[end], arr[start]

    # Swap the elements with pivot
    arr[pivot_idx], arr[end+1] = arr[end+1], arr[pivot_idx]
    return end + 1

def quicksort(arr, start, end):
    if start < end:
        # Partition the list
        split = inplace_qsort(arr, start, end)

        # Sort both halves
        print(arr)
        quicksort(arr, start, split - 1)
        print(arr)
        quicksort(arr, split + 1, end)

    return arr

def read(read_fn):
    read_fn()
    line = read_fn().split()
    arr = [int(i) for i in line]
    return arr

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            arr = read(f.readline)
    else:
        arr = read(input)

    arr = quicksort(arr, 0, len(arr) - 1)
    for i in arr:
        print(i, end=' ')

    print("")

if __name__ == "__main__":
    main()