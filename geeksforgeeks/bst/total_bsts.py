def num_trees(N):
    if len(N) <= 2:
        return len(N)

    total = 0
    for i in N:
        low = []
        high = []
        for j in N:
            if j < i:
                low.append(j)
            elif j > i:
                high.append(j)
        low_count = num_trees(low)
        high_count = num_trees(high)
        low_count = low_count if low_count > 0 else 1
        high_count = high_count if high_count > 0 else 1
        total += low_count * high_count
    return total

if __name__ == '__main__':
     n = 5
     input = [i+1 for i in range(n)]
     print(num_trees(input))
