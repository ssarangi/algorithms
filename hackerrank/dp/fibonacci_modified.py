__author__ = 'sarangis'

'''
https://www.hackerrank.com/challenges/fibonacci-modified
'''

def fibonacci_modified(n_plus_one, n, num_els):
    if num_els == 0:
        return n_plus_one

    n_plus_two = n_plus_one ** 2 + n
    return fibonacci_modified(n_plus_two, n_plus_one, num_els - 1)

def main():
    inputstr = input()
    l = [int(i) for i in inputstr.split(' ')]
    a, b, n = l[0], l[1], l[2]
    v = fibonacci_modified(b, a, n - 2)
    print(v)

if __name__ == "__main__":
    main()
