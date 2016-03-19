def binary_search_sorted_array(arr, el, start, end):
    # array is rotated by k elements and it is sorted to begin with.
    # This makes the binary search a little difficult.
    mid = (start + end) // 2
    if arr[mid] == el:
        return mid

    if start == end:
        return None

    elif el > arr[mid]:
        return binary_search_sorted_array(arr, el, mid+1, end)
    else:
        return binary_search_sorted_array(arr, el, start, mid)


arr = [11, 13, 15, 1, 2, 4, 5, 9]
k = 3
# Find the start and end position
# Since the array is rotated lets compare the 0th element and the kth element
el = 3
if arr[0] <= el <= arr[k - 1]:
    idx = binary_search_sorted_array(arr, el, 0, k-1)
else:
    idx = binary_search_sorted_array(arr, el, k, len(arr) - 1)

print(idx)
