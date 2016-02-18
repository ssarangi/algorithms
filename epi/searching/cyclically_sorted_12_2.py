# Find O(log n) algorithm for finding smallest element
def cyclically_sorted_search(arr, start, end):
    center = (start + end) // 2
    print("(" + str(arr[start]) + ", " + str(start) + ")", "(" + str(arr[end]) + ", " + str(end) + ")")

    if start == end or abs(start - end) == 1:
        return min(arr[start], arr[end])

    if arr[start] > arr[end] and arr[center] > arr[end]:
        # Shift the search to the right
        return cyclically_sorted_search(arr, center, end)
    else:
        return cyclically_sorted_search(arr, start, center)


def main():
    arr = [378, 478, 550, 631, 800, 900, 1100, 1200, 103, 203, 220, 234, 279, 368]
    print(cyclically_sorted_search(arr, 0, len(arr) - 1))

if __name__ == "__main__":
    main()