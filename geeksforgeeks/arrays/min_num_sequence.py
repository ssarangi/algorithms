def min_num(sequence):
    # max num needed = len(sequence)
    max_num = len(sequence)
    val = ""
    for i in range(len(sequence), 0, -1):
        cc = sequence[i]
        if cc == "D":
            max_num -= 2
        else:
            val = str(max_num)

def main():
    pass
    
if __name__ == "__main__":
    main()