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

# TODO: NOT_COMPLETE

import sys


def create_2d_arr(width, height):
    arr = [[0 for i in range(0, width)] for j in range(0, height)]
    return arr


def max_width(grid, x, y, grid_max_width):
    if grid[y][x] == 'x':
        return 0

    if x == len(grid[0]) - 1:
        return 0

    if grid_max_width[y][x+1] == 'x':
        return 0
    else:
        return 1 + grid_max_width[y][x+1]


def max_height(grid, x, y, grid_max_height):
    if x == 3 and y == 2:
        a = 10

    if grid[y][x] == 'x':
        return 0

    if y == len(grid) - 1:
        return 0

    if grid_max_height[y+1][x] == 'x':
        return 0
    else:
        return 1 + grid_max_height[y+1][x]


def print_grid(grid, x, y, width, height):
    for iy in range(y, y + height + 1):
        s = ""
        for ix in range(x, x + width + 1):
            s += grid[iy][ix]

        print(s)


def k_marsh(grid, grid_max_width, grid_max_height):
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
            mw = max_width(grid, ix, iy, grid_max_width)
            # mh = min(max_height(grid, ix, iy, grid_max_height), max_height(grid, ix + mw, iy, grid_max_height))

            if ix == 4 and iy == 2:
                b = 10

            if ix == 1 and iy == 0:
                a = 10

            mh = max_height(grid, ix + mw, iy, grid_max_height)
            cp = 2 * (mh + mw)

            for i in reversed(range(1, mw)):
                tmp = max_height(grid, ix + i, iy, grid_max_height)
                cp1 = 2 * i * tmp
                if cp1 > cp:
                    mh = min(mh, max_height(grid, ix + i, iy, grid_max_height))
                    mw = i

            grid_max_width[iy][ix] = mw
            grid_max_height[iy][ix] = mh

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

    print("From DP: Max X: %s\tMax Y: %s\tPerimeter: %s\tMax W: %s\tMax H: %s" % (max_x + 1, max_y + 1, perimeter, max_w, max_h))
    print_grid(grid, max_x, max_y, max_w, max_h)

    return perimeter

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

    grid_max_width = create_2d_arr(grid_cols, grid_rows)
    grid_max_height = create_2d_arr(grid_cols, grid_rows)

    max_perimeter = k_marsh(grid, grid_max_width, grid_max_height)
    print(max_perimeter)

if __name__ == "__main__":
    main()