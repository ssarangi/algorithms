def count_combinations(k, score_ways):
    combinations = [0] * (k+1)
    combinations[0] = 1 # One way to reach 0

    for score in score_ways:
        for j in range(score, k+1):
            combinations[j] += combinations[j - score]


    return combinations[k]

def main():
    possibilities = [2, 3, 7]
    sum = 12
    print(count_combinations(sum, possibilities))

if __name__ == "__main__":
    main()