class Solution(object):
    def lengthOfLongestSubstring_brute_force(self, s):
        if len(s) == 0:
            return 0
        
        seen = set()
        longest = 0
        current = 0
        
        start = 0
        cn = start
        while cn < len(s):
            c = s[cn]
            if c not in seen:
                current += 1
                cn += 1
                seen.add(c)
            else:
                current = 0
                start += 1
                seen.clear()
                cn = start
                
            longest = max(longest, current)
                
        return longest

    def lengthOfLongestSubstring(self, s):
        """
        dp[i]: Length of longest substring at position i
        postdict: to record each characters last position in the input string s
        How to obtain dp[i] from dp[i-1]

        1) if s[i] not in postdict - s[i] is apparently different from s[i-1], so dp[i] = dp[i-1] + 1
        2) if s[i] already in postdict - for example s[i] = 'b', s[i-1] = 'a', from postdict we know the
        latest b position is j, and s[j+1] till s[i-1] will not be b. So dp[i] = i - postdict[s[i]]? Wait, if there
        is a 2nd 'a' in between two 'b' ? In this case dp[i] = dp[i-1] + 1. So we have min() here.
        Example: b***...***ab
        Finally, we need to update postdict with s[i] position
        """
        if not s:
            return 0

        dp = [1] * len(s)
        postdict = {s[0]: 0}
        longest = 1

        for i in range(1, len(s)):
            if s[i] in postdict:
                dp[i] = min(dp[i-1] + 1, i - postdict[s[i]])
            else:
                dp[i] = dp[i-1] + 1

            postdict[s[i]] = i
            longest = max(longest, dp[i])

        return longest

soln = Solution()
s = "abcabcbb"
print(soln.lengthOfLongestSubstring(s))

s = "bbbbbbb"
print(soln.lengthOfLongestSubstring(s))

s = "aab"
print(soln.lengthOfLongestSubstring(s))

s = "dvdf"
print(soln.lengthOfLongestSubstring(s))

s = "tmmzuxt"
print(soln.lengthOfLongestSubstring(s))

s = "eee"
print(soln.lengthOfLongestSubstring(s))