# https://leetcode.com/problems/regular-expression-matching/

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "":
            return False

        class Pattern:
            def __init__(self, p):
                self.char = p
                self.repeat = False
                self.next = None

            def __str__(self):
                return self.char + " " + " --> Repeatable: %s" % (self.repeat)

            __repr__ = __str__

        def create_pattern_list(p):
            patterns = []

            last_pattern = None

            for c in p:
                if c == '*':
                    if last_pattern == None:
                        raise Exception("Invalid pattern encountered")

                    last_pattern.repeat = True
                else:
                    curr_pattern = Pattern(c)
                    patterns.append(curr_pattern)
                    if last_pattern is not None:
                        last_pattern.next = curr_pattern

                    last_pattern = curr_pattern

            return patterns

        def matches(p, c):
            if p.char == ".":
                return True

            return p.char == c

        def match_helper(p, s, idx):
            # We have pattern left which is a repeat and we have run out of characters to match.
            if idx >= len(s) and p is not None and p.repeat is True:
                return True

            # We have characters left but we have run out of patterns
            if p is None and idx < len(s):
                return False

            # Current pattern is none so return True
            if p is None and idx >= len(s):
                return True

            if p.repeat:
                if matches(p, s[idx]):
                    first = match_helper(p, s, idx + 1)
                    next_idx = idx + 1
                else:
                    first = True # We have matched 0 instances of repeatable character which doesn't exist
                    next_idx = idx
                second = match_helper(p.next, s, next_idx)

                return first | second
            else:
                return matches(p, s[idx]) & match_helper(p.next, s, idx+1)

        patterns = create_pattern_list(p)
        final = match_helper(patterns[0], s, 0)
        return final


soln = Solution()

import unittest


class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testRegex(self):
        self.assertEqual(soln.isMatch("aa", "a"), False)
        self.assertEqual(soln.isMatch("aa", "aa"), True)
        self.assertEqual(soln.isMatch("aaa", "aa"), False)
        self.assertEqual(soln.isMatch("aa", "a*"), True)
        self.assertEqual(soln.isMatch("aa", ".*"), True)
        self.assertEqual(soln.isMatch("ab", ".*"), True)
        self.assertEqual(soln.isMatch("aab", "c*a*b"), True)


if __name__ == "__main__":
    unittest.main()