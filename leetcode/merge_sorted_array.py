class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        def shift_by_n(arr, start, end, n):
            assert len(arr) >= end + n
            prev = arr[start]
            for i in range(start, end):
                nxt = arr[i + n]
                arr[i + n] = prev
                prev = nxt
            
            return arr, end + n
        
        if n == 0:
            return
        
        p1 = 0
        p2 = 0
        considered_p1 = 0
        
        end_arr1 = m
        
        cnt_merge = True
        while cnt_merge:
            if considered_p1 >= m or nums1[p1] > nums2[p2]:
                nums1, end_arr1 = shift_by_n(nums1, p1, end_arr1, 1)
                nums1[p1] = nums2[p2]
                p2 += 1
            else:
                considered_p1 += 1
                
            p1 += 1
            if p1 == len(nums1) or p2 == len(nums2):
                cnt_merge = False
    
soln = Solution()

m1 = [1, 5, 9, 10, None, None, None, None]
m2 = [2, 4, 6, 8]

m1 = [1, None]
m2 = [2]

m1 = [1]
m2 = []

# print(soln.merge(m1, 4, m2, len(m2)))
print(soln.merge(m1, 1, m2, len(m2)))