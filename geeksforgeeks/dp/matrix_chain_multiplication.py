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

# TODO: Incomplete

def matrix_chain_multiplication(p):
    pass

def main():
    p = [(40, 20),(20, 30), (30, 10), (10, 30)]

if __name__ == "__main__":
    main()