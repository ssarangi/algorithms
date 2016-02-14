def max_difference(arr):
    max_diff = 0
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            max_diff = max(max_diff, abs(arr[i] - arr[j]))

    return max_diff

def main():
    z_coords = [2, 3, 5, 1, 6]
    print(max_difference(z_coords))

if __name__ == "__main__":
    main()
