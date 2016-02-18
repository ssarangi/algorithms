def intersection(arr1, arr2):
    i1 = 0
    i2 = 0

    seen = {}
    new_arr = []
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] == arr2[i2]:
            if arr1[i1] not in seen:
                new_arr.append(arr1[i1])
            seen[arr1[i1]] = True
            i1 += 1
            i2 += 1
        elif arr1[i1] > arr2[i2]:
            i2 += 1
        else:
            i1 += 1

    return new_arr

def main():
    a1 = [1, 3, 5, 7, 9, 11, 13, 15, 16, 17, 19, 20]
    a2 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

    print(intersection(a1, a2))

if __name__ == "__main__":
    main()