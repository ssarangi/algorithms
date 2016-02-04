__author__ = 'sarangis'

'''
https://www.hackerrank.com/challenges/coin-change
'''
def all_multiples(el, k):
    arr = []
    counter = 1
    while True:
        res = el * counter
        if res <= k:
            arr.append(res)
        else:
            break

        counter += 1

    return arr

def coin_change(k, els):
    # Create all possible ways in which we can select the same element multiple times
    prevarr = []
    total_ways_to_sum = 0
    for el in els:
        if el > k:
            continue
        elif el == k:
            total_ways_to_sum += 1
            continue

        multiples_arr = all_multiples(el, k)

        newarr = [el for el in prevarr] + [el for el in multiples_arr]
        newarr = sorted(newarr)
        if len(prevarr) > 0:
            for multiple in multiples_arr:
                for p in prevarr:
                    sum = p + multiple

                    if sum < k:
                        newarr.append(sum)
                    elif sum == k:
                        total_ways_to_sum += 1
                    else:
                        break
                # else:
                #     continue
                # break

        prevarr = sorted(newarr)

    return total_ways_to_sum

import sys

def read(read_fn):
    sum, N = [int(v) for v in read_fn().replace("\n", "").strip().split(" ")]
    coins = [int(coin) for coin in read_fn().replace("\n", "").strip().split(" ")]

    return coins, sum

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            coins, sum = read(f.readline)
    else:
        coins, sum = read(input)

    total_possible_ways = coin_change(sum, coins)
    print(total_possible_ways)

if __name__ == "__main__":
    main()
