import unittest

def get_hash(nums):
    nums = sorted(nums)
    new_num = 0
    for idx, num in enumerate(nums):
        new_num += num * pow(10, idx)
        
    return new_num

def three_number_sum(arr):
    num_dict = set()
    result = []
    added = set()
    
    for n in arr: num_dict.add(n)
    
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            s = arr[i] + arr[j]
            if -s in num_dict:
                new_num = get_hash([arr[i], arr[j], -s])
                if new_num not in added:
                    result.append([arr[i], arr[j], -s])
                    added.add(new_num)
    
    return list(result)

class UnitTest(unittest.TestCase):
    def testThreeNumbers(self):
        self.assertEqual(three_number_sum([2, 3, 1, -2, -1, 0, 2, -3, 0]),
                                          [[2, -2, 0],
                                           [1, -1, 0],
                                           [3, -2, -1],
                                           [3, 0, -3]])
                                           
if __name__ == "__main__":
    unittest.main()