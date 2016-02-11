"""
http://www.geeksforgeeks.org/count-inversions-in-an-array-set-2-using-self-balancing-bst/
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted
then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.

Two elements a[i] and a[j] form an inversion if
     a[i] > a[j] and i < j. For simplicity, we may
     assume that all elements are unique.

     Example:
     Input:  arr[] = {8, 4, 2, 1}
     Output: 6
     Given array has six inversions (8,4), (4,2),
     (8,2), (8,1), (4,1), (2,1).
"""

def inversions_naive(arr):
    # Try the brute force approach
    inversions = []
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inversions.append((arr[i], arr[j]))

    return inversions

def merge(a1, a2):
    inversions = []
    new_arr = [0] * (len(a1) + len(a2))
    i = 0
    j = 0
    k = 0
    while i < len(a1) or j < len(a2):
        if j == len(a2):
            for m in a2:
                inversions.append(a1[i], m)
            new_arr[k] = a1[i]
            i += 1
        elif i == len(a1):
            new_arr[k] = a2[j]
            j += 1
        elif a1[i] <= a2[j]:
            new_arr[k] = a1[i]
            i += 1
        else:
            for m in range(i, len(a1)):
                inversions.append((a1[m], a2[j]))
            new_arr[k] = a2[j]
            j += 1

        k += 1

    return new_arr, inversions

def merge_sort(arr):
    if len(arr) == 1:
        return arr, []

    q = len(arr) // 2

    # Dividing the array into 2 parts
    a1 = arr[:q]
    a2 = arr[q:]

    a1, inv1 = merge_sort(a1)
    a2, inv2 = merge_sort(a2)

    arr, inversions = merge(a1, a2)
    return arr, inversions

def avl_tree(arr):
    pass

def main():
    a1 = [2, 4, 1, 3, 5]
    print(inversions_naive(a1))
    print(merge_sort(a1))

if __name__ == "__main__":
    main()