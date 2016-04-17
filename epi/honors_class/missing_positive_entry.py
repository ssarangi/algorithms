def missing_positive_entry(arr):
    arr = sorted(arr)
    
    idx = 0
    curr_num = arr[0]
    while idx < len(arr):
        if arr[idx] == curr_num:
            idx += 1
            curr_num += 1
            if curr_num == 0:
                curr_num += 1
        else:
            return curr_num
            
    return None

arr = [3, 5, 4, -1, 5, 1, -1]

print(missing_positive_entry(arr))