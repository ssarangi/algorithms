# https://careercup.com/question?id=5687065971785728
import unittest

def find_anagrams(list_strings):
    unique_strs = {}
    for s in list_strings:
        sstr = "".join(sorted(s))
        if sstr in unique_strs:
            unique_strs[sstr].append(s)
        else:
            unique_strs[sstr] = [s]
    
    results = []
    for k,v in unique_strs.items():
        if len(v) > 1:
            for i in v:
                results.append(i)
                
    return results

class UnitTest(unittest.TestCase):
    def testAnagrams(self):
        self.assertEqual(find_anagrams(["tea", "ate", "eat", "apple", "java", "vaja", "cut", "utc"]),
                                       ['java', 'vaja', 'tea', 'ate', 'eat', 'cut', 'utc'])
                                       
if __name__ == "__main__":
    unittest.main()