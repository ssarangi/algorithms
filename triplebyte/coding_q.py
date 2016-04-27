# Find the set of all linear combinations that can be done on a set of numbers
# to reach a target sum
# +,-,*,/ operations

def linear_combinations(arr, total_sum):
    def compute_linear_combinations(arr, current_idx, prev_sum, prev_ops, visited_set, results):
        """
        arr: Current array
        current_idx: Current Index of which array
        prev_sum: Previous sum till now
        prev_ops: Prev operations string
        visited_set: indexes already used
        results: Array of prev operations
        """
        if current_idx in visited_set:
            return
        
        visited_set.add(current_idx)
        
        for i in range(0, 4):
            s = prev_ops
            op = ops[i]
            current_sum = op(prev_sum, arr[current_idx])
            s += ops_str[i] + str(arr[current_idx])
            
            if current_sum == total_sum:
                results.append(s)
            
            tmp_visited = set([i for i in visited_set])
            
            for j in range(0, len(arr)):
                compute_linear_combinations(arr, j, current_sum, s, tmp_visited, results)
    
    results = []
    compute_linear_combinations(arr, 0, 0, "", set(), results)
    print(results)

a = [1, 5, 3, 8, 9, 10, 20, 25, 22, 28]

ops = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x / y,
]

ops_str = [
    '+',
    '-',
    '*',
    '/'
]

linear_combinations(a, 50)
