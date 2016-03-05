def zigzag(arr):
    lt = lambda x, y: x < y
    gt = lambda x, y: x > y

    aux_arr = []
    lambda__ = [lt, gt]
    for i in range(0, len(arr) - 1):
        aux_arr.append(lambda__[i % 2])

    i = 0
    while i < len(arr) - 1:
        if not aux_arr[i](arr[i], arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]

        i += 1

    return arr

def main():
    arr = [4, 3, 7, 8, 6, 2, 1]
    print(zigzag(arr))

if __name__ == "__main__":
    main()