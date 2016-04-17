def gcd(a, b):
    def gcd_(a, b, considered):
        if a > 0:
            a -= considered

        if b > 0:
            b -= considered

        if a == 0 and b == 0:
            return True

        if 0 < a < considered or 0 < b < considered:
            return False

        return gcd_(a, b, considered)

    considered = min(a, b)
    for i in range(considered, 0, -1):
        if gcd_(a, b, i):
            return i

    return 1

a = 54
b = 24
print(gcd(a, b))