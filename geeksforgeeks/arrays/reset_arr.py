def reset_arr(arr, idx):
    length = len(idx)

    for i, idx_el in enumerate(idx):
        arr[idx_el], arr[i] = arr[i], arr[idx_el]
        idx[idx_el], idx[i] = idx[i], idx[idx_el]

    return arr, idx

def main():
    arr = [50, 40, 70, 60, 90]
    idx = [3, 0, 4, 1, 2]
    print(reset_arr(arr, idx))
    arr = [10, 11, 12]
    idx = [1, 0, 2]
    print(reset_arr(arr, idx))

if __name__ == "__main__":
    main()