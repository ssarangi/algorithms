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
                self.any_character = (p == '.')
                self.repeat = False
                
            def __str__(self):
                return self.char + " " + " --> Repeatable: %s" % (self.repeat) + " --> any_character: %s" % (self.any_character)
            
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
                    if last_pattern is not None:
                        patterns.append(last_pattern)
                        
                    last_pattern = Pattern(c)
            
            patterns.append(last_pattern)
            return patterns
        
        def char_matches(c, p):
            if c == p.char or p.any_character == True:
                return True
            
            return False

        def match(s, p, patterns):
            pass

        patterns = create_pattern_list(p)
        patterns.reverse()
        
        cp = None
        cidx = 0
        
        while cidx < len(s):
            c = s[cidx]
            if cp is None or cp.repeat is False:
                if len(patterns) == 0:
                    return False
                
                cp = patterns.pop()
            
            if not char_matches(c, cp):
                # In this case, check if the pattern is repeatable
                # If it is not then we cannot match it. If the pattern is not repeatable
                # then we return False otherwise we get a new pattern if it exists
                if cp.repeat == False:
                    return False
                elif len(patterns) == 0:
                    return False

                # Turn the repeat off so that we can pop off the next pattern
                cp.repeat = False
            else:
                cidx += 1

        if len(patterns) > 0:
            return False

        return True
            
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

