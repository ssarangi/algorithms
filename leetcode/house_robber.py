class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
            
        if len(nums) == 1:
            return nums[0]
            
        max_v = nums[0]
        
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = nums[1]

        if nums[1] > max_v:
            max_v = nums[1]
        
        for i in range(2, len(nums)):
            mv = nums[0]
            for j in range(0, i - 1):
                if mv < dp[j]:
                    mv = dp[j]
                    
            dp[i] = mv + nums[i]
            
            if max_v < dp[i]:
                max_v = dp[i]

        return max_v
    
soln = Solution()
nums = [5, 8, 10, 2, 3]
nums = [2, 1, 1, 1, 5]
nums = [1, 2, 1, 1]
print(soln.rob(nums))
