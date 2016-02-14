# Use O(1) space complexity and O(n) time complexity
def sort_left_right(arr, i):
    for cntr, el in enumerate(arr):
        if arr[cntr] > arr[i]:
            pass

def main():
    a1 = [3,4,2,5,9,8,0]
    i = 3
    print(sort_left_right(a1, i))

if __name__ == "__main__":
    main()
