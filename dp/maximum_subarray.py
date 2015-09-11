__author__ = 'sarangis'

'''
https://www.hackerrank.com/challenges/maxsubarray
'''

def maximum_contiguous_subarray(L):
    current_sum = 0
    current_index = -1
    best_sum = 0
    best_start_index = -1
    best_end_index = -1

    for i in range(len(L)):
        val = current_sum + L[i]
        if val > 0:
            if current_sum == 0:
                current_index = i
            current_sum = val
        else:
            current_sum = 0

        if current_sum > best_sum:
            best_sum = current_sum
            best_start_index = current_index
            best_end_index = i

    return L[best_start_index: best_end_index + 1]

def maximum_noncontiguous_subarray(L):
    best_list = []

    current_sum = 0
    for i in L:
        current_sum += i
        if current_sum > current_sum - i:
            best_list.append(i)

    return best_list

def main():
    test_cases = int(input())

    for i in range(0, test_cases):
        N = int(input())
        arr = [int(num) for num in (input().split(' '))]
        contiguous = maximum_contiguous_subarray(arr)
        non_contiguous = maximum_noncontiguous_subarray(arr)
        s1 = sum(contiguous)
        s2 = sum(non_contiguous)
        print("%s %s" % (s1, s2))

if __name__ == "__main__":
    main()
