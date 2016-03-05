def is_edit_distance_one_with_hash_table(s1, s2):
    hash_table = {}
    for c in s1:
        if c in hash_table:
            hash_table[c] += 1
        else:
            hash_table[c] = 1

    num_differences = 0
    for c in s2:
        if c not in hash_table:
            num_differences += 1
        else:
            hash_table[c] -= 1
            if hash_table[c] == 0:
                del hash_table[c]

    return num_differences == 1, num_differences

def is_edit_distance_one(s1, s2):
    p1 = 0
    p2 = 0

    num_differences = 0
    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1
        elif s1[p1] != s2[p2]:
            if len(s1) > len(s2):
                # This is an insertion in p2.
                p1 += 1
                num_differences += 1
            elif len(s1) < len(s2):
                p2 += 1
                num_differences += 1
            else:
                # Both the lengths are the same. This means that the character is to be replaced
                num_differences += 1
                p1 += 1
                p2 += 1

    num_differences += len(s1) - p1 + len(s2) - p2
    return num_differences == 1, num_differences

def main():
    s1 = "geek"
    s2 = "geeks"
    print(is_edit_distance_one(s1, s2))

    s1 = "geeks"
    s2 = "geeks"
    print(is_edit_distance_one(s1, s2))

    s1 = "geaks"
    s2 = "geeks"
    print(is_edit_distance_one(s1, s2))

    s1 = "peaks"
    s2 = "geeks"
    print(is_edit_distance_one(s1, s2))

if __name__ == "__main__":
    main()