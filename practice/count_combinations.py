def count_combinations_recursive(total, possible):
    if total == 0:
        return 1

    comb_so_far = 0
    for el in possible:
        if total < el:
            continue

        comb_so_far += count_combinations_recursive(total - el, possible)

    return comb_so_far

def count_combinations_dp(total, possible):
    dp = [0] * (total + 1)

    for i in range(1, total + 1):
        for el in possible:
            idx = max(0, i - el)
            if i == el:
                dp[i] += dp[idx] + 1
            else:
                dp[i] += dp[idx]        

    return dp[total]


total = 2
possible = [2, 3, 7]

for i in range(0, 13):
    total = i
    print("-" * 50)
    print(count_combinations_recursive(total, possible))
    print(count_combinations_dp(total, possible))
    print("-" * 50)