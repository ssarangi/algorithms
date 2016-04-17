def primes(num):
    res = []
    multiples = {}
    for i in range(2, num):
        # If the i is in the dict then ignore
        if i not in multiples:
            res.append(i)

            j = 1
            while i * j < num:
                multiples[i*j] = True
                j += 1
        
    return res

print(primes(24))