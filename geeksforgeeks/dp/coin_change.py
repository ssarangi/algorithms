"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm}
valued coins, how many ways can we make the change? The order of coins doesn’t matter.
"""
def get_multiples(N, coin):
    multiples = []
    counter = 1
    same_val = 0
    while True:
        val = coin * counter
        if val > N:
            break

        if val == N:
            same_val += 1

        multiples.append(val)
        counter += 1

    return same_val, multiples

def coin_change(N, S):
    S = sorted(S)
    total_combinations = 0

    prev_coin_multiples = None
    for coin in S:
        matched, coin_multiples = get_multiples(N, coin)
        total_combinations += matched

        new_coin_multiples = [comb for comb in coin_multiples]
        if prev_coin_multiples is not None:
            new_coin_multiples = [comb for comb in prev_coin_multiples] + new_coin_multiples
            # Find all the additions to the new one
            for c1 in prev_coin_multiples:
                for c2 in coin_multiples:
                    if c1 + c2 <= N and (c1 + c2) not in new_coin_multiples:
                        new_coin_multiples.append(c1 + c2)

                    if c1 + c2 == N:
                        total_combinations += 1

        prev_coin_multiples = new_coin_multiples

    return total_combinations



def main():
    N = 4
    S = [1,2,3]
    print(coin_change(N, S))

    N = 10
    S = [2,5,3,6]
    print(coin_change(N, S))

if __name__ == "__main__":
    main()