# https://leetcode.com/problems/word-break/

import unittest


# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: Set[str]
#         :rtype: bool
#         """
#         curr_word = ""
#         for c in s:
#             curr_word += c
#             if curr_word in wordDict:
#                 curr_word = ""

#         if len(curr_word) > 0:
#             return False

#         return True

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # Initialize all the dp values as 0
        dp = [False] * (len(s) + 1)

        for i in range(1, len(s) + 1):

            # If dp[i] is false and then check if the current prefix can make it
            # true
            prefix = s[0:i]
            if dp[i] is False and prefix in wordDict:
                dp[i] = True

            # if dp[i] is true then check for all substrings starting from i+1 char
            # and store their result
            if dp[i] is True:
                # If we reached the last prefix
                if i == len(s):
                    return True

                for j in range(i+1, len(s) + 1):
                    suffix = s[i: j]
                    if dp[j] is False and suffix in wordDict:
                        dp[j] = True

                    # If we reached the last character
                    if j == len(s) and dp[j] is True:
                        return True

        # Print the DP table
        # print("\n".join(str(i) for i in dp))
        return False


class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testWordBreak(self):
        self.assertEqual(self.soln.wordBreak("leetcode", {"leet", "code"}), True)
        self.assertEqual(self.soln.wordBreak("aaaaaaa", {"aaaa", "aaa"}), True)
        self.assertEqual(self.soln.wordBreak(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            {"a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"}), False)
        self.assertEqual(self.soln.wordBreak("abcd", {"a","abc","b","cd"}), True)

if __name__ == "__main__":
    unittest.main()