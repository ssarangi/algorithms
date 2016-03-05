def swap_elements(arr, index, el1_idx, el2_idx):
    el1 = arr[el1_idx]
    el2 = arr[el2_idx]

    arr[el1_idx], arr[el2_idx] = arr[el2_idx], arr[el1_idx]
    index[el1] = el2_idx
    index[el2] = el1_idx
    return arr, index

def min_swaps(arr, index, hash_table, start, swaps_so_far):
    if start >= len(arr):
        return swaps_so_far

    if hash_table[arr[start]] == arr[start+1]:
        return min_swaps(arr, index, hash_table, start + 2, swaps_so_far)

    second_el = arr[start + 1]
    first_el = arr[start]

    # Try swapping the second element
    first_el_pair = hash_table[first_el]
    index_first_el_pair = index[first_el_pair]

    arr, index = swap_elements(arr, index, start + 1, index_first_el_pair)
    min_first_el_swaps = min_swaps(arr, index, hash_table, start + 2, swaps_so_far + 1)
    # Revert the change
    arr, index = swap_elements(arr, index, start + 1, index_first_el_pair)

    # Try swapping the first element
    second_el_pair = hash_table[second_el]
    index_second_el_pair = index[second_el_pair]

    arr, index = swap_elements(arr, index, start, index_second_el_pair)
    min_second_el_swaps = min_swaps(arr, index, hash_table, start + 2, swaps_so_far + 1)
    # Revert the change
    arr, index = swap_elements(arr, index, start, index_second_el_pair)

    return min(min_first_el_swaps, min_second_el_swaps)

def main():
    pairs = [(1, 3), (2, 6), (4, 5)]
    arr = [3, 5, 6, 4, 1, 2]

    # Create dictionaries which list the pairs
    hash_table = {}
    for pair in pairs:
        hash_table[pair[0]] = pair[1]
        hash_table[pair[1]] = pair[0]

    # Create an index for each position
    index = {}
    for i, el in enumerate(arr):
        index[el] = i

    print(min_swaps(arr, index, hash_table, 0, 0))

if __name__ == "__main__":
    main()