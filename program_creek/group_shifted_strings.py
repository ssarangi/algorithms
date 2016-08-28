def get_shifted_char(c, shift):
    ascii = ord(c) - ord('a')
    shifted_char_ascii = 0
    if ascii + shift >= 26:
        shifted_char_ascii = ascii + shift - 26
    else:
        shifted_char_ascii = ascii + shift

    shifted_char = chr(shifted_char_ascii + ord('a'))
    return shifted_char


def get_new_string(orig, diff):
    s = ""
    for c in orig:
        s += get_shifted_char(c, diff)

    return s


def group_shifted_strings(sl):
    visited = set()
    hash_dict = set(sl)
    results = []

    for s in sl:
        if s not in visited:
            curr_str_res = [s]
            for diff in range(1, 26):
                snew = get_new_string(s, diff)
                if snew in hash_dict:
                    visited.add(snew)
                    curr_str_res.append(snew)

            results.append(curr_str_res)

    return results


import unittest


class UnitTest(unittest.TestCase):
    def testGroupShiftedStrings(self):
        self.assertEqual(group_shifted_strings(["abc", "bcd", "xyz", "az", "ba", "acef", "a", "z"]),
                         [["abc", "bcd", "xyz"], ["az", "ba"], ["acef"], ["a", "z"]])


if __name__ == "__main__":
    unittest.main()