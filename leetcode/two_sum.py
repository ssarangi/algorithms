def two_sum(nums, target):
    dict_nums = {}
    idx1 = -1
    idx2 = -1
    
    for i, el in enumerate(nums):
        dict_nums[el] = i
        
    for i, n in enumerate(nums):
        if target - n in dict_nums:
            idx1 = i
            idx2 = dict_nums[target - n]
            
            if idx1 == idx2:
                continue
            return [idx1, idx2]
        
    return None

nums = [2, 7, 11, 15]
target = 9

nums = [3, 2, 4]
target = 6

print(two_sum(nums, target))