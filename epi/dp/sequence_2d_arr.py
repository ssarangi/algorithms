# [1, 2, 3]
# [3, 4, 5]
# [5, 6, 7]
# -----------------------
# [1, 3, 4, 6] Pattern to recognize
#

def sequence_exists(arr, pattern):
    return False

def sequence(arr, pattern, pattern_fnd, i, j, pidx = 0):
    num_cols = len(arr[0])
    num_rows = len(arr)

    if pidx == len(pattern):
        return pattern_fnd

    all_patterns = []

    for cx in range(-1, 2, 2):
        for cy in range(-1, 2, 2):
            if arr[i][j] == pattern[pidx]:
                pattern_fnd.append(arr[i][j])
                patt = sequence(arr, pattern, pattern_fnd, pidx+1)
                all_patterns.append(patt)

    return all_patterns

def main():
    arr = [[1, 2, 3],
           [3, 4, 5],
           [5, 6, 7]]

    pattern = [1, 3, 4, 6]

    print(sequence(arr, pattern, 0, 0, [], 0))
    
if __name__ == "__main__":
    main()