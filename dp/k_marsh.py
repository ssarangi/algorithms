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

    perimeter = 0

    grid_rows = len(grid)
    grid_cols = len(grid[0])

    for ix in reversed(range(0, grid_cols)):
        for iy in reversed(range(0, grid_rows)):
            grid_max_width[iy][ix] = max_width(grid, ix, iy, grid_max_width)
            grid_max_height[iy][ix] = max_height(grid, ix, iy, grid_max_height)

            current_perimeter = 0
            if grid_max_width[iy][ix] > 0 and grid_max_height[iy][ix] > 0:
                current_perimeter = grid_max_width[iy][ix] * 2 + grid_max_height[iy][ix] * 2

            perimeter = max(perimeter, current_perimeter)

    if perimeter == 0:
        perimeter = "impossible"

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

    grid_max_width = [[0] * grid_cols] * grid_rows
    grid_max_height = [[0] * grid_cols] * grid_rows

    max_perimeter = k_marsh(grid, 0, 0, grid_max_width, grid_max_height)
    print(max_perimeter)

if __name__ == "__main__":
    main()