class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        substrs = []
        table = [[0] * len(s) for i in range(0, len(s))]
        
        # Generate all the substrings
        for length in range(1, len(s) + 1):
            new_substrs = []
            for start in range(0, len(s) - 1):
                end = min(len(s) - 1, start + length - 1)
                if s[start] == s[end]:
                    if length == 1 or length == 2:
                        table[start][end] = 1
                    else:
                        table[start][end] = table[start+1][end-1]
                        
                    if table[start][end] == 1:
                        new_substrs.append(s[start:end+1])
            
            if len(new_substrs) > 0:
                substrs.append(new_substrs)
        
        return substrs

soln = Solution()

s = "cdd"
all_substrs = soln.partition(s)

for ss in all_substrs:
    print(ss)