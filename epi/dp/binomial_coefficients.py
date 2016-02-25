def binomial_coefficients(num_rows):
    arr = [[0 for i in range(0, num_rows)] for j in range(0, num_rows + 1)]
    for i in range(0, num_rows):
        arr[i][0] = 1
        arr[i][i] = 1

    for i in range(1, num_rows + 1):
        for j in range(1, i):
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    return arr

def main():
    num_rows = 6
    bin_coeff = binomial_coefficients(num_rows)
    for i in range(0, num_rows):
        print(bin_coeff[i])

    
if __name__ == "__main__":
    main()