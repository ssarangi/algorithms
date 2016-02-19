# Perform a DFS on this graph
def compute_path(maze, visited, path, all_paths, start, end):
    if start == end:
        all_paths.append(path)
        return path

    # Any point might have a maximum of 4 different positions to choose from
    for idx in range(0, 4):
        x = 0
        y = 0
        if idx == 0:
            x = -1
        elif idx == 1:
            y = -1
        elif idx == 2:
            x = 1
        else:
            y = 1

        cx = start[0] + x
        cy = start[1] + y

        if cx < 0 or cx == len(maze[0]):
            continue

        if cy < 0 or cy == len(maze):
            continue

        if maze[cy][cx] == 'B':
            continue

        if (cx, cy) not in visited:
            # Make a copy of the visited path and add the current point
            nv = set([i for i in visited])
            nv.add((cx, cy))
            np = [i for i in path]
            np.append((cx, cy))
            p = compute_path(maze, nv, np, all_paths, (cx, cy), end)

            # if p is not None:
            #     # We found a path. so return this
            #     return p

    # No such path exists
    return None

def draw_path(maze, path):
    for c in path:
        maze[c[1]] = maze[c[1]][:c[0]] + "." + maze[c[1]][c[0]+1:]

def print_maze(maze):
    s = ""
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            s += maze[i][j] + " "

        s += "\n"

    print(s)

def main():
    maze = [
        "B     BB E",
        "  B       ",
        "B B  BB BB",
        "   BBB  B ",
        " BB       ",
        " BB       ",
        "    B     ",
        "B B B B   ",
        "B BB   BBB",
        "S      BB ",
    ]

    start = (0, 9)
    end = (9, 0)

    all_paths = []
    p = compute_path(maze, [start], [start], all_paths, start, end)

    for path in all_paths:
        copy_maze = [row for row in maze]
        draw_path(copy_maze, path)
        print_maze(copy_maze)

if __name__ == "__main__":
    main()