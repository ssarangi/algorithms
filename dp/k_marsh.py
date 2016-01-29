"""
The MIT License (MIT)

Copyright (c) 2015 <Satyajit Sarangi>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

"""
https://www.hackerrank.com/challenges/mr-k-marsh
"""

import sys

def find_max_perimeter(grid, x, y):
    l_max_width = 0
    l_max_height = 0
    for i in range(y, len(grid)):
        if grid[i][x] == '.':
            l_max_height += 1
        else:
            break

    for i in range(x, len(grid[0])):
        if grid[y][i] == '.':
            l_max_width += 1
        else:
            break

    perimeter = 2 * (l_max_width - 1) + 2 * (l_max_height - 1)
    return perimeter, l_max_width - 1, l_max_height - 1

def max_width(grid, x, y, grid_max_width):
    if  grid[y][x] == 'x':
        return -1

    if x == len(grid[0]) - 1:
        return 0

    return 1 + grid_max_width[y][x+1]

def max_height(grid, x, y, grid_max_height):
    if grid[y][x] == 'x':
        return -1

    if y == len(grid) - 1:
        return 0

    return 1 + grid_max_height[y+1][x]

def k_marsh(grid, x, y, grid_max_width, grid_max_height):
    # At this current location find the maximum width height we can attain
    max_x = -1
    max_y = -1
    max_w = -1
    max_h = -1

    perimeter = 0

    grid_rows = len(grid)
    grid_cols = len(grid[0])

    for ix in reversed(range(0, grid_cols)):
        for iy in reversed(range(0, grid_rows)):
            if ix == 13 and iy == 67:
                a = 10

            grid_max_width[iy][ix] = max_width(grid, ix, iy, grid_max_width)
            grid_max_height[iy][ix] = max_height(grid, ix, iy, grid_max_height)

            current_perimeter = 0
            if grid_max_width[iy][ix] > 0 and grid_max_height[iy][ix] > 0:
                current_perimeter = grid_max_width[iy][ix] * 2 + grid_max_height[iy][ix] * 2

            if current_perimeter > perimeter:
                max_x = ix
                max_y = iy
                max_w = grid_max_width[iy][ix]
                max_h = grid_max_height[iy][ix]

            perimeter = max(perimeter, current_perimeter)


    if perimeter == 0:
        perimeter = "impossible"

    print("From DP: Max X: %s\tMax Y: %s\tPerimeter: %s\tMax W: %s\tMax H: %s" % (max_x, max_y, perimeter, max_w, max_h))

    return perimeter

def fn_max_perimeter(grid):
    max_p = 0
    max_x = -1
    max_y = -1
    max_w = -1
    max_h = -1

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            perimeter, mw, mh = find_max_perimeter(grid, x, y)

            if perimeter > max_p:
                max_p = perimeter
                max_x = x
                max_y = y
                max_w = mw
                max_h = mh

    print( "From BF: Max X: %s\tMax Y: %s\tPerimeter: %s\tMax_W: %s\tMax_H: %s" % (max_x, max_y, max_p, max_w, max_h))


def read(read_fn):
    m, n = [int(v) for v in read_fn().split(" ")]
    grid = []
    for i in range(0, m):
        row = read_fn().replace("\n", "")
        grid.append(row)

    return grid

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            grid = read(f.readline)
    else:
        grid = read(input)

    grid_rows = len(grid)
    grid_cols = len(grid[0])

    grid_max_width = [[0] * grid_cols] * grid_rows
    grid_max_height = [[0] * grid_cols] * grid_rows

    max_perimeter = k_marsh(grid, 0, 0, grid_max_width, grid_max_height)
    fn_max_perimeter(grid)
    print(max_perimeter)

if __name__ == "__main__":
    main()