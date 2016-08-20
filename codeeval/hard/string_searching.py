import sys


class Char:
    def __init__(self, c):
        self.c = c
        self.repeat = False

    def set_repeat(self):
        self.repeat = True

    def match(self, char):
        if self.c == char or self.repeat is True:
            return True
        return False

    def __str__(self):
        return self.c


def create_characters(substr):
    char_list = []
    for idx, c in enumerate(substr):
        if c == '\\':
            continue
        if c == '*' and substr[idx - 1] == '\\':
            char_cls = Char('*')
        elif c == '*':
            char_cls = Char("*")
            char_cls.set_repeat()
        else:
            char_cls = Char(c)

        char_list.append(char_cls)

    return char_list


# def string_searching_helper(orig, orig_idx, char_list, char_list_idx):
#     if orig_idx >= len(orig) or char_list_idx >= len(char_list):
#         return False
#
#     curr_match = char_list[char_list_idx].match(orig[orig_idx])
#
#     if char_list[char_list_idx].repeat is True:
#         if curr_match is not False:
#             curr_match = string_searching_helper(orig, orig_idx + 1, char_list, char_list_idx)
#
#         if char_list_idx < len(char_list):
#             curr_match |= string_searching_helper(orig, orig_idx, char_list, char_list_idx + 1)
#
#     elif orig_idx < len(orig) and char_list_idx < len(char_list):
#         curr_match = string_searching_helper(orig, orig_idx + 1, char_list, char_list_idx + 1)
#
#     return curr_match

def string_searching_helper(orig, orig_idx, char_list, char_list_idx):
    curr_pattern = char_list[char_list_idx]
    continue_matching = not curr_pattern.repeat
    curr_match = True
    while continue_matching:
        curr_match = curr_pattern.match(orig[orig_idx])
        if curr_match is False:
            return False

        orig_idx += 1
        char_list_idx += 1
        if char_list_idx < len(char_list) and orig_idx < len(orig):
            curr_pattern = char_list[char_list_idx]
            continue_matching = not curr_pattern.repeat
        else:
            continue_matching = False

    # So at this point, we have 3 cases
    # 1) We ran out of strings to match
    # 2) We ran out of patterns to use
    # 3) We are currently hitting a repeat so we should be doing a recursive function call

    if char_list_idx >= len(char_list):
        return curr_match

    # Case 1: We ran out of strings to match
    if orig_idx >= len(orig):
        # Check if there is only 1 pattern left and that one is a STAR
        if char_list_idx < len(char_list) - 1 and char_list[char_list_idx + 1].repeat:
            return curr_match
        else:
            return False

    # # Case 2: We ran out of patterns to match
    # curr_pattern = char_list[char_list_idx]
    # if not curr_pattern.repeat:
    #     return False

    # Case 3: We are at a repeat. So we need to split at this point and run recursively
    if orig_idx + 1 < len(orig):
        curr_match = string_searching_helper(orig, orig_idx + 1, char_list, char_list_idx)

    if char_list_idx + 1 < len(char_list):
        curr_match |= string_searching_helper(orig, orig_idx, char_list, char_list_idx + 1)

    return curr_match


def string_searching(full_str):
    orig, substr = full_str.split(",")
    char_list = create_characters(substr)
    start_idx = 0
    found_match = False

    while start_idx < len(orig) and found_match is False:
        found_match = string_searching_helper(orig, start_idx, char_list, 0)
        start_idx += 1

    return found_match

# Rishi provided a very simple and elegant solution to this problem. The idea is
# to split the pattern at the *. Then find the substring locations and if all
# the substrings occur in the string then its a match
def split(pattern):
    patterns = []

    prev = None
    curr_str = ""
    for c in pattern:
        if c == '\\':
            prev = c
            continue
        elif c != '*' or (c == '*' and prev == '\\'):
            curr_str += c
        elif c == '*':
            patterns.append(curr_str)
            curr_str = ""

        prev = c

    patterns.append(curr_str)
    return patterns


def find_first_occurence(string, substring):
    initial_pos = -1
    for i in range(0, len(string)):
        initial_pos = i
        for j in range(0, len(substring)):
            if string[i + j] != substring[j]:
                initial_pos = -1
                break

        if initial_pos != -1:
            break

    return initial_pos


def rishi_string_search(full_str):
    string, pattern = full_str.split(",")
    patterns = split(pattern)

    for pattern in patterns:
        # Find the first position of the string
        pos = find_first_occurence(string, pattern)
        if pos != -1:
            string = string[pos + len(pattern) + 1:]
        else:
            return False

    return True


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            test = test.replace("\n", "")
            match = string_searching(test)
            match1 = rishi_string_search(test)
            if match != match1:
                print("Values do not match: " + test)
            print(str(match).lower())

            # import unittest


            # class UnitTest(unittest.TestCase):
            #     def testStringSearching(self):
            #         self.assertEqual(string_searching("Hello,ell"), True)
            #         self.assertEqual(string_searching("This is good, is"), True)
            #         self.assertEqual(string_searching("aaaab,a*b"), True)
            #         self.assertEqual(string_searching("CodeEval,C*Eval"), True)
            #         self.assertEqual(string_searching("Old,Young"), False)
            #         self.assertEqual(string_searching("PQYARSqAynqv AZ 9Lh2 lOq v2kH4NwX,*2kH4N"), True)
            #         self.assertEqual(string_searching("w2WILmbM0qETRigSZ dVfSSsI4OFZMjv,fSF2IjISs MZmVOTdR"), False)


            # if __name__ == "__main__":
            #     unittest.main()