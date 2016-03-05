def zigzag(string, n):
    new_s = [[""] for i in range(0, n)]
    row = 0
    dir = "down"
    for c in string:
        new_s[row] += c
        if row == n - 1:
            row -= 1
            dir = "up"
        elif row == 0:
            row += 1
            dir = "down"
        elif dir == "up":
            row -= 1
        else:
            row += 1

    final_str = ""
    for i in new_s:
        for c in i:
            final_str += c

    return final_str

def main():
    s = "ABCDEFGH"
    print(zigzag(s, 2))

    s = "GEEKSFORGEEKS"
    print(zigzag(s, 3))

if __name__ == "__main__":
    main()