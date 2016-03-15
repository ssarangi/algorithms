from queue import Queue

def connected_cell(matrix):
    max_rows = len(matrix)
    max_cols = len(matrix[0])

    q = Queue()
    visited = {}

    max_cell_size = 0
    for j in range(0, max_rows):
        for i in range(0, max_cols):
            if (i, j) not in visited and matrix[j][i]:
                q.put((i, j))

                cell_size = 0
                while not q.empty():
                    x, y = q.get()
                    if (x, y) in visited:
                        continue

                    cell_size += 1
                    visited[(x, y)] = True

                    if x-1 >= 0 and matrix[y][x-1]:
                        q.put((x-1, y))

                    if y-1 >= 0 and matrix[y-1][x]:
                        q.put((x, y-1))

                    if x+1 < max_cols and matrix[y][x+1]:
                        q.put((x+1, y))

                    if y+1 < max_rows and matrix[y+1][x]:
                        q.put((x, y+1))

                    if x+1 < max_cols and y+1 < max_rows and matrix[y+1][x+1]:
                        q.put((x+1, y+1))

                    if x-1 >= 0 and y+1 < max_rows and matrix[y+1][x-1]:
                        q.put((x-1, y+1))

                    if x-1 >= 0 and y-1 >= 0 and matrix[y-1][x-1]:
                        q.put((x-1, y-1))

                max_cell_size = max(max_cell_size, cell_size)

    return max_cell_size


import sys

def read(read_fn):
    M = int(read_fn())
    N = int(read_fn())
    matrix = []
    for i in range(0, M):
        line = read_fn().split()
        arr = [int(i) for i in line]
        matrix.append(arr)

    return matrix

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            matrix = read(f.readline)
    else:
        matrix = read(input)

    largest_cell = connected_cell(matrix)
    print(largest_cell)

if __name__ == "__main__":
    main()