def binary_search_first_occurrence(arr, search_val, start, end):
    center = (start + end) // 2

    if arr[center] == search_val:
        prev = center
        while arr[center] == search_val:
            prev = center
            center -= 1
        return search_val, prev
    elif center <= start or center >= end:
        return -1
    elif search_val < arr[center]:
        return binary_search_first_occurrence(arr, search_val, start, center)
    else:
        return binary_search_first_occurrence(arr, search_val, center + 1, end)

def main():
    arr = [-14, 10, 2, 108, 108, 243, 285, 285, 285, 401]
    arr = sorted(arr)
    print(arr)
    print(binary_search_first_occurrence(arr, 285, 0, len(arr) - 1))

if __name__ == "__main__":
    main()