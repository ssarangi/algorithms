import sys

def max_difference_brute_force(arr):
    max_diff = 0
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            max_diff = max(max_diff, abs(arr[i] - arr[j]))

    return max_diff

def max_difference(arr):
    # Find the min and max in the arr
    min_v = sys.maxsize
    max_v = -sys.maxsize
    for i in arr:
        min_v = min(min_v, i)
        max_v = max(max_v, i)

    # The max difference is
    return max_v - min_v

def main():
    z_coords = [2, 3, 5, 1, 6]
    print(max_difference_brute_force(z_coords))
    print(max_difference(z_coords))

if __name__ == "__main__":
    main()
