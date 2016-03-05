def ones_complement(binary):
    new_s = ""
    for c in binary:
        if c == "0":
            new_s += "1"
        else:
            new_s += "0"

    return new_s

def twos_complement(binary):
    ones_comp = ones_complement(binary)

    # We have to add 1 to get the 2's complement
    new_s = ""
    carry = 1
    reversed  = ones_comp[::-1]
    for c in reversed:
        if c == "0":
            if carry == 1:
                new_s += "1"
            else:
                new_s += "0"
            carry = 0
        else:
            if carry == 1:
                new_s += "0"
            else:
                new_s += "1"

    new_s = new_s[::-1]
    return new_s

def main():
    s = "0111"
    print(ones_complement(s))
    print(twos_complement(s))

if __name__ == "__main__":
    main()