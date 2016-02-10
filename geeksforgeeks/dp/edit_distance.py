def insert(s, c):
    s = c + s
    return s

def remove(s):
    s = s[1:]
    return s

def replace(s, c):
    s = c + s[1:]
    return s

def edit_distance_recursive(s1, s2):
    if s1 == "" or s2 == "":
        return 0

    if s1[0] == s2[0]:
        return edit_distance_recursive(s1[1:], s2[1:])

    max_distance = min(1 + edit_distance_recursive(insert(s1, s2[0]), s2),
                       1 + edit_distance_recursive(remove(s1), s2),
                       1 + edit_distance_recursive(replace(s1, s2[0]), s2))

    return max_distance

def edit_distance_dp(s1, s2):
    dp_arr = [[0 for i in range(0, len(s1) + 1)] for j in range(0, len(s2) + 1)]
    pass

def main():
    t1 = ["geek", "gesek"]
    ed = edit_distance_recursive(t1[0], t1[1])
    print(ed)
    ed = edit_distance_dp(t1[0], t1[1])
    print(ed)

if __name__ == "__main__":
    main()