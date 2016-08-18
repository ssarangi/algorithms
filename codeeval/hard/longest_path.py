# https://www.codeeval.com/open_challenges/182/

import sys
import math

def longest_path_helper(matrix, visited, curr, path):
    x = curr[0]
    y = curr[1]

    curr_id = matrix[y][x]
    if matrix[y][x] in visited:
        return len(visited)

    xmin = max(0, x - 1)
    xmax = min(len(matrix) - 1, x + 1)

    ymin = max(0, y - 1)
    ymax = min(len(matrix) - 1, y + 1)

    if matrix[y][xmin] in visited and \
                    matrix[y][xmax] in visited and \
                    matrix[ymin][x] in visited and \
                    matrix[ymax][x] in visited:
        path += curr_id
        return path

    visited.add(matrix[y][x])
    path += matrix[y][x]

    finalpath = path
    paths = [(xmin, y), (xmax, y), (x, ymin), (x, ymax)]

    for i in range(0, 4):
        xt = paths[i][0]
        yt = paths[i][1]
        if matrix[yt][xt] in visited:
            continue

        new_visited = set(visited)
        new_path = path
        new_path = longest_path_helper(matrix, new_visited, (xt, yt), new_path)
        if len(new_path) > len(finalpath):
            finalpath = new_path

    return finalpath


def longest_path(s):
    n_square = len(s)
    n = int(math.sqrt(n_square))
    matrix = [[0] * n for _ in range(0, n)]

    for y in range(0, n):
        for x in range(0, n):
            idx = y * n + x
            matrix[y][x] = s[idx]

    finalpath = ""
    for y in range(0, n):
        for x in range(0, n):
            visited = set()
            path = ""
            path = longest_path_helper(matrix, visited, (x, y), path)
            if len(path) > len(finalpath):
                finalpath = path

    return finalpath


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        path = longest_path(test)
        print(len(path))
