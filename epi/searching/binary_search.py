def binary_search(arr, search_val, start, end):
    center = (start + end) // 2

    if arr[center] == search_val:
        return search_val, center
    elif search_val < arr[center]:
        return binary_search(arr, search_val, start, center)
    else:
        return binary_search(arr, search_val, center + 1, end)

def main():
    arr = [1, 5, 2, 6, 9, 4, 10, 2, 19]
    arr = sorted(arr)
    print(arr)
    print(binary_search(arr, 6, 0, len(arr) - 1))

if __name__ == "__main__":
    main()