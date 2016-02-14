def get_mapping(digit):
    mapping = {
        1: "1",
        2: "ABC",
        3: "DEF",
        4: "GHI",
        5: "JKL",
        6: "MNO",
        7: "PQRS",
        8: "TUV",
        9: "WXYZ",
        0: "0"
    }

    return mapping[digit]

def char_seq(ph_no):
    n = ph_no[0]
    seq = get_mapping(int(n))

    if len(ph_no) == 1:
        return [c for c in seq]

    all_strs = char_seq(ph_no[1:])
    new_strs = []
    for s in seq:
        for new_str in all_strs:
            new_strs.append(s + new_str)

    return new_strs

def main():
    p1 = "2276696"
    print(char_seq(p1))

if __name__ == "__main__":
    main()
