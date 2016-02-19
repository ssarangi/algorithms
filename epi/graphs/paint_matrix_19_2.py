def color_recursive(maze, pos, color_type, recursion_depth = 0):
    print("Recursion Depth: %s" % recursion_depth)
    maze[pos[1]] = maze[pos[1]][:pos[0]] + color_type + maze[pos[1]][pos[0] + 1:]

    for counter in range(0, 4):
        x = 0
        y = 0
        if counter == 0:
            x = -1
        elif counter == 1:
            y = -1
        elif counter == 2:
            x = 1
        elif counter == 3:
            y = 1

        cx = pos[1] + x
        cy = pos[0] + y

        if cx < 0 or cx == len(maze[0]):
            continue

        if cy < 0 or cy == len(maze):
            continue

        if maze[cy][cx] == color_type:
            color_recursive(maze, (cx, cy), color_type, recursion_depth + 1)

    return None

from queue import Queue


def color(maze, start, color_type):
    if color_type == ".":
        flip_color = "B"
    else:
        flip_color = "."

    q = Queue()
    q.put(start)

    visited = set()
    while not q.empty():
        pos = q.get()

        if pos in visited:
            continue

        visited.add(pos)

        maze[pos[1]] = maze[pos[1]][:pos[0]] + flip_color + maze[pos[1]][pos[0] + 1:]

        for counter in range(0, 4):
            x = 0
            y = 0
            if counter == 0:
                x = -1
            elif counter == 1:
                y = -1
            elif counter == 2:
                x = 1
            elif counter == 3:
                y = 1

            cx = pos[0] + x
            cy = pos[1] + y

            if cx < 0 or cx == len(maze[0]):
                continue

            if cy < 0 or cy == len(maze):
                continue

            if maze[cy][cx] == color_type:
                q.put((cx, cy))


def print_maze(maze):
    s = ""
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            s += maze[i][j] + " "

        s += "\n"

    print(s)


def main():
    maze = [
        "B.B...BBBB",
        "..B..B..BB",
        "BBB..BB.BB",
        ".B.BBBB.B.",
        "B.B....B..",
        "B.B..B.BBB",
        "....B.B..B",
        "B.B.B.B...",
        "B.BB...BBB",
        ".......BB."
    ]

    start = (4, 5)
    color(maze, start, maze[start[1]][start[0]])
    print_maze(maze)

if __name__ == "__main__":
    main()