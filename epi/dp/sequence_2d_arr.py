# [1, 2, 3]
# [3, 4, 5]
# [5, 6, 7]
# -----------------------
# [1, 3, 4, 6] Pattern to recognize
#

def sequence(arr, pattern, seen_before, x, y, pidx = 0):
    num_cols = len(arr[0])
    num_rows = len(arr)

    if (x, y) in seen_before:
        return seen_before[(x, y, pidx)]

    if pidx == len(pattern) - 1:
        if pattern[pidx] == arr[y][x]:
            return True

        return False

    if arr[y][x] != pattern[pidx]:
        return False

    found = False
    for cx in range(-1, 2):
        for cy in range(-1, 2):
            if abs(cx) == 1 and abs(cy) == 1:
                continue

            if 0 <= x + cx < num_cols and 0 <= y + cy < num_rows:
                found |= sequence(arr, pattern, seen_before, x+cx, y+cy, pidx+1)

    seen_before[(x,y, pidx)] = found

    return found

def main():
    arr = [[1, 2, 3],
           [3, 4, 5],
           [5, 6, 7]]

    pattern = [1, 3, 4, 6]

    print(sequence(arr, pattern, {}, 0, 0, 0))
    
if __name__ == "__main__":
    main()