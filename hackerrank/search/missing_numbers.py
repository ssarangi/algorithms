def missing_numbers(A, B):
    B_dict = {}
    for el in B:
        if el in B_dict:
            B_dict[el] += 1
        else:
            B_dict[el] = 1

    A_dict = {}
    for el in A:
        if el in A_dict:
            A_dict[el] += 1
        else:
            A_dict[el] = 1

    new_arr = []
    for k,v in B_dict.items():
        if k not in A_dict:
            new_arr.append(k)
        elif A_dict[k] != v:
            new_arr.append(k)

    new_arr = sorted(new_arr)
    return new_arr

import sys

def read(read_fn):
    M = int(read_fn())
    line = read_fn().split()
    arr1 = [int(i) for i in line]
    N = int(read_fn())
    line = read_fn().split()
    arr2 = [int(i) for i in line]

    return arr1, arr2

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            A, B = read(f.readline)
    else:
        A, B = read(input)

    missing_num = missing_numbers(A, B)
    for num in missing_num:
        print(num, end=" ")

if __name__ == "__main__":
    main()