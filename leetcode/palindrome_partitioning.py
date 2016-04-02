class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def get_substr(s, n):
            substr = ""
            for i in range(0, len(s)):
                if (n and (1 << i)) > 0:
                    substr += s[i]
                    print("Substring: " + substr)
                    
            return substr
        
        def generate_substrings(s):
            l = len(s)
            all_strs = []
            for i in range(1, 2 ** l - 1):
                all_strs.append(get_substr(s, i))
            
            return all_strs
        
        all_strs = generate_substrings(s)
        for s in all_strs:
            print(s)
    
soln = Solution()

s = "aab"
soln.partition(s)