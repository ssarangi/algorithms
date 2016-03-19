class Pattern:
    def __init__(self, ch, repeated=False):
        self.ch = ch
        self.repeated = repeated
        self.match_all = False

    def __str__(self):
        return str(self.ch) + ": Repeated --> " + str(self.repeated)

    __repr__ = __str__

def create_pattern_list(pattern):
    ps = 0
    last_pattern = None
    patterns = []
    while ps < len(pattern):
        if pattern[ps] == "*":
            if last_pattern is None:
                last_pattern = Pattern('')
                last_pattern.match_all = True
                patterns.append(last_pattern)

            last_pattern.repeated = True
        else:
            last_pattern = Pattern(pattern[ps])
            patterns.append(last_pattern)

        ps += 1

    return patterns

def isMatch(s, pattern):
    patterns = create_pattern_list(pattern)
    patterns += [None] * (len(s) - len(patterns))
    assert len(patterns) > 0
    spos = 0
    ploc = 0

    cp = patterns[0]
    while cp is not None and spos < len(s) and ploc < len(patterns):
        cp = patterns[ploc]

        if cp is None:
            return False

        cc = s[spos]
        if cp.ch != cc and not cp.match_all:
            if cp.repeated == False:
                return False
            else:
                if ploc + 1 < len(patterns):
                    ploc += 1
                else:
                    return False
        else:
            # Increment the position of the char pos
            spos += 1
            if not cp.repeated:
                ploc += 1

    if spos < len(s):
        return False

    return True

def main():
    print(isMatch("aa","a"))
    print(isMatch("aa","aa"))
    print(isMatch("aaa","aa"))
    print(isMatch("aa", "a*"))
    print(isMatch("aa", "*"))
    print(isMatch("ab", "*"))
    print(isMatch("ab", "*"))
    print(isMatch("a",  "b*a"))
    print(isMatch("a", "a*a"))
    print(isMatch("aab", "c*a*b"))
    
if __name__ == "__main__":
    main()