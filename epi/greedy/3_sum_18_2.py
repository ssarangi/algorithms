def find_k_combinations(arr, k, current_combination, combinations):
    if k == len(current_combination):
        combinations.append(current_combination)
        return

    for i in arr:
        # Create a copy of the current combination
        tcc = [i for i in current_combination]
        tcc.append(i)
        find_k_combinations(arr, k, tcc, combinations)


def three_sum(A, T, k):
    # Now see as we iterate over the list to see if we can find a sum
    for i in range(0, len(A)):
        combinations = []
        find_k_combinations(A[i: i + k + 1], k, [], combinations)

        for combination in combinations:
            if sum(combination) == T:
                print(combination)
                return True

    return False

def main():
    A = [1, 4, 6, 2, 8, 5, 0, 7, 3]
    T = 15
    k = 3

    print(three_sum(A, T, k))


if __name__ == "__main__":
    main()