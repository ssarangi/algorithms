def spiral_ordering(arr):
    total_rows_cols = len(arr) * len(arr[0])
    row = 0
    col = 0
    max_rows = len(arr)
    max_cols = len(arr[0])

    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4

    direction = RIGHT

    visited = {}

    result = []

    # Now start spiralling
    while len(visited) < total_rows_cols:
        print(row, col)
        result.append(arr[row][col])
        visited[(row, col)] = True

        if direction == RIGHT:
            col  = min(max_cols - 1, col + 1) if (row, col + 1) not in visited else col
            if col == max_cols or (row, col) in visited:
                direction = DOWN
                row += 1
        elif direction == DOWN:
            row = min(max_rows - 1, row + 1) if (row + 1, col) not in visited else row
            if row == max_rows or (row, col) in visited:
                direction = LEFT
                col -= 1
        elif direction == LEFT:
            col = max(0, col - 1) if (row, col - 1) not in visited else col
            if col < 0 or (row, col) in visited:
                direction = UP
                row -= 1
        elif direction == UP:
            row = max(0, row - 1) if (row - 1, col) not in visited else row
            if row < 0 or (row, col) in visited:
                direction = RIGHT
                col += 1

    return result

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiral_ordering(arr))