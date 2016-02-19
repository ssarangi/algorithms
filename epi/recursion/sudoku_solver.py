def is_valid(arr):
    if arr is None:
        return False

    for y in range(0, 9):
        row_exist = set()
        for x in range(0, 9):
            if arr[y][x] != 0 and arr[y][x] in row_exist:
                return False

            row_exist.add(arr[y][x])

    for x in range(0, 9):
        col_exist = set()
        for y in range(0, 9):
            if arr[y][x] != 0 and arr[y][x] in col_exist:
                return False

            col_exist.add(arr[y][x])

    # Now try all the 3x3 squares
    counter = 0
    x = 0
    y = 0

    while counter < 9:
        exists = set()
        for j in range(0, 3):
            for i in range(0, 3):
                if arr[j][i] != 0 and arr[j][i] in exists:
                    return False
                exists.add(arr[j][i])

        x += 3
        if x > 6:
            x = 0

        counter += 1
        y += 3

    return True

def is_full(arr):
    for y in range(0, 9):
        for x in range(0, 9):
            if arr[y][x] == 0:
                return False

    return True

def deep_copy(arr):
    new_arr = [[arr[y][x] for x in range(0, 9)] for y in range(0, 9)]
    return new_arr

def sudoku(arr, recursion_level=0):
    print(recursion_level)
    if is_full(arr):
        return arr

    if not is_valid(arr):
        return None

    for y in range(0, 9):
        for x in range(0, 9):
            if arr[y][x] == 0:
                # This is an empty spot. So try putting a number here
                for i in range(1, 10):
                    # Create a copy of the array
                    new_arr = deep_copy(arr)
                    new_arr[y][x] = i

                    # Check if this is valid
                    if is_valid(new_arr):
                        new_arr = sudoku(new_arr, recursion_level + 1)
                        if is_valid(new_arr) and is_full(new_arr):
                            return new_arr

    return None

def main():
    arr = [
        [0, 0, 3, 0, 2, 0, 6, 0, 0],
        [9, 0, 0, 3, 0, 5, 0, 0, 1],
        [0, 0, 1, 8, 0, 6, 4, 0, 0],
        [0, 0, 8, 1, 0, 2, 9, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 6, 7, 0, 8, 2, 0, 0],
        [0, 0, 2, 6, 0, 9, 5, 0, 0],
        [8, 0, 0, 2, 0, 3, 0, 0, 9],
        [0, 0, 5, 0, 1, 0, 3, 0, 0]
    ]

    new_arr = sudoku(arr)

    for y in range(0, 9):
        print(new_arr[y])

if __name__ == "__main__":
    main()