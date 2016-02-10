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

    if grid[y][x+1] == 'x':
        return 0
    else:
        return 1 + grid_max_width[y][x+1]


def max_height(grid, x, y, grid_max_height):
    if grid[y][x] == 'x':
        return 0

    if y == len(grid) - 1:
        return 0

    if grid[y+1][x] == 'x':
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

    max_perimeter = 0

    grid_rows = len(grid)
    grid_cols = len(grid[0])
    grid_max_perimeter = create_2d_arr(grid_cols, grid_rows)

    for ix in reversed(range(0, grid_cols)):
        for iy in reversed(range(0, grid_rows)):
            if ix == 1 and iy == 0:
                a = 10

            # Figure out the max width and height at this point
            mw = max_width(grid, ix, iy, grid_max_width)
            mh = max_height(grid, ix, iy, grid_max_height)

            grid_max_width[iy][ix] = mw
            grid_max_height[iy][ix] = mh

            if mh == 0 or mw == 0:
                continue

            # Now try to find the biggest rectangular area with this information.
            current_max_w = 0
            current_max_h = 0
            cmw = mw
            cmh = mh
            for i in reversed(range(1, cmw + 1)):
                mh = cmh
                for j in reversed(range(1, cmh + 1)):
                    tmp_height = max_height(grid, ix + i, iy, grid_max_height)
                    current_max_h = max(current_max_h, tmp_height)

                    # At this height figure out the max width and make sure that it is equal to the current width
                    tmp_width = max_width(grid, ix, iy + j, grid_max_width)
                    current_max_w = max(current_max_w, tmp_width)

                    # Make sure all the width and heights are greater than 0.
                    # Verify the height we get from the other side is the same as
                    # this side. (mh == tmp)
                    # if tmp_width > 0 and tmp_height > 0 and tmp_height >= (mh - (grid_rows - (iy + j))) and tmp_width >= (mw - (grid_cols - (ix + i))):
                    if tmp_width > 0 and tmp_width > 0 and tmp_width >= mw and tmp_height >= mh:
                        cp = 2 * (i + j)
                        if cp > max_perimeter:
                            max_perimeter = cp
                            max_w = i
                            max_h = j
                            max_x = ix
                            max_y = iy

                    mh -= 1
                    # Find the largest perimeter contained within (ix, iy) and (ix + mw, ix + mh)

                mw -= 1

                grid_max_perimeter[iy][ix] = max_perimeter

    if max_perimeter == 0:
        max_perimeter = "impossible"

    # print("From DP: Max X: %s\tMax Y: %s\tPerimeter: %s\tMax W: %s\tMax H: %s" % (max_x, max_y, max_perimeter, max_w, max_h))
    # print_grid(grid, max_x, max_y, max_w, max_h)

    return max_perimeter

def read(read_fn):
    m, n = [int(v) for v in read_fn().split(" ")]
    grid = []
    for i in range(0, m):
        row = read_fn().replace("\n", "")
        row = [i for i in row]
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