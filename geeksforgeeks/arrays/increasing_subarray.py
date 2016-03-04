def find_increasing_subarrays(arr):
    total = 0

    i = 0
    start = 0
    while start < len(arr) - 1:
        j = i + 1
        while j < len(arr) - 1 and arr[i] < arr[j]:
            j += 1
            i += 1

        num_els = j - start + 1
        for ii in range(1, num_els):
            total += ii
        start = j
        i = start

    return total

def main():
    arr = [1,2,3,4]
    print(find_increasing_subarrays(arr))

    
if __name__ == "__main__":
    main()