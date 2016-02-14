# Use O(1) space complexity and O(n) time complexity
def sort_left_right(arr, pivot):
    pivot_el = arr[pivot]
    # First swap the pivot element
    arr[pivot], arr[len(arr) - 1] = arr[len(arr)-1], arr[pivot]

    # Now start looping through the array to see if we can swap all the elements
    pivot = len(arr) - 1
    i = 0
    j = len(arr) - 2

    while i < j:
        if arr[i] < pivot_el:
            i += 1
        elif arr[j] > pivot_el:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]

    # Now restore the pivot element position
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return arr

def main():
    a1 = [3,6,2,5,9,8,1,0]
    i = 3
    print(sort_left_right(a1, i))

if __name__ == "__main__":
    main()
