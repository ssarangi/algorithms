# Given a string, find the longest substring which is palindrome. For example, if the given string
# is “forgeeksskeegfor”, the output should be “geeksskeeg”.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 1
        palin_start = 0
        
        for start in range(1, len(s) - 1):
            mismatch = False
            p1 = start

            if len(s) % 2 == 0:
                p2 = start + 1
            else:
                p2 = start

            current_len = 0
            while not mismatch:
                if s[p1] != s[p2]:
                    mismatch = True
                else:
                    p1 -= 1
                    p2 += 1
                    current_len += 1
                    
                    if current_len > max_len:
                        max_len = current_len
                        palin_start = start
                    
                    if p1 < 0 or p2 >= len(s):
                        mismatch = True
                        
        return s[palin_start - max_len + 1 : palin_start + max_len + 1]

s = "forgeeksskeegfor"
s = "abb"
soln = Solution()
print(soln.longestPalindrome(s))