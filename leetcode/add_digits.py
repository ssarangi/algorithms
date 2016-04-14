class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
            
        s = 0
        while num > 0:
            s += num % 10
            num = num // 10
        
        return self.addDigits(s)
    
soln = Solution()

n = 38
print(soln.addDigits(n))