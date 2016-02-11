"""
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not
actually to perform the multiplications, but merely to decide in which order to perform the multiplications.
We have many options to multiply a chain of matrices because matrix multiplication is associative. In other words,
no matter how we parenthesize the product, the result will be the same. For example, if we had four matrices A, B, C,
and D, we would have:

    (ABC)D = (AB)(CD) = A(BCD) = ....

However, the order in which we parenthesize the product affects the number of simple arithmetic operations needed to
compute the product, or the efficiency. For example, suppose A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is
a 5 × 60 matrix. Then,

    (AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
    A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.


"""

# A     B      C       D
#    a     b       c
#       d      e
#          f

import sys

def matrix_chain_multiplication(p):
    num_matrices = len(p)
    dp = p

    # Augment the dp array
    # So the augmented value is 0
    dp = [0 for i in range(0, num_matrices)]

    # Now start creating the triangle
    for j in range(0, len(dp) - 1):
        new_dp = [0] * (len(dp) - 1)

        min_v = sys.maxsize
        min_idx = -1
        for i in range(0, num_matrices - 1):
            num_operations = p[i][0] * p[i][1] * p[i+1][1]
            fin_res = num_operations + min(dp[i], dp[i+1])
            new_dp[i] = fin_res

            if min_v > fin_res:
                min_v = fin_res
                min_idx = i

        p[min_idx][1] = p[min_idx+1][1]
        p.remove(p[min_idx+1])

        dp = new_dp
        num_matrices = num_matrices - 1

    assert len(dp) == 1
    return dp[0]

def main():
    p = [[40, 20],[20, 30], [30, 10], [10, 30]]
    print(matrix_chain_multiplication(p))

if __name__ == "__main__":
    main()