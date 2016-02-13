def stoi(s):
    len_of_str = len(s)
    power = len_of_str - 1
    final_num = 0
    for c in s:
        if ord(c) < 48 or ord(c) > 57:
            raise Exception("Invalid integer encoding: %s" % s)

        num = ord(c) - 48
        final_num += (10 ** power) * num
        power -= 1

    return final_num

def itos(num):
    repr = ""
    while num > 0:
        digit = num % 10
        num = num // 10
        repr = str(digit) + repr

    return repr

def main():
    print(stoi("123"))
    # print(stoi("123abc"))
    print(itos(123456))

if __name__ == "__main__":
    main()
