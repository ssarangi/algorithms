import sys

def consecutive_max_diff(arr):
    new_arr = [0] * len(arr)
    min_v = sys.maxsize
    max_v = -sys.maxsize

    for i in range(0, len(arr) - 1):
        new_arr[i+1] = arr[i+1] + arr[i]
        min_v = min(min_v, new_arr[i+1])
        max_v = max(max_v, new_arr[i+1])

    return max_v - min_v

def main():
    arr = [1,5,6,7,3,4,9,8]
    print(consecutive_max_diff(arr))

if __name__ == "__main__":
    main()
