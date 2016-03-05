def flip_zeros(arr, m):
    current_not_flipped = m
    start = 0
    max_till_now = 0
    positions = []
    best_positions = None
    cons_zero = 0
    end_of_zeros = -1

    while 0 <= start < len(arr):
        i = start
        while (i < len(arr)) and (current_not_flipped != 0 or arr[i] != 0):
            if arr[i] == 0:
                current_not_flipped -= 1
                positions.append(i)
                if current_not_flipped == 0:
                    end_of_zeros = i + 1

            cons_zero += 1
            i += 1

        if cons_zero > max_till_now:
            best_positions = [p for p in positions]
            max_till_now = cons_zero

        positions.clear()
        cons_zero = 0
        current_not_flipped = m
        start = end_of_zeros
        end_of_zeros = -1

    return max_till_now, best_positions


def main():
    arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    m = 2
    print(flip_zeros(arr, m))
    arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    m = 1
    print(flip_zeros(arr, m))
    arr = [0, 0, 0, 1]
    m = 4
    print(flip_zeros(arr, m))

if __name__ == "__main__":
    main()