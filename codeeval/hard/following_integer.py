import sys

def create_number(digits):
    ss = "".join([str(d) for d in digits])
    num = int(ss)
    return num

def is_number_thousands(digits):
    for i in range(1, len(digits)):
        if digits[i] > 0:
            return False

    return True

def find_non_zero_idx(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] > 0:
            return i

    return -1

def find_following_integer(num_as_str):
    digits = [int(d) for d in num_as_str]

    minidx = len(digits) - 1

    swap_idx = [False, -1, -1]

    while minidx >= 0:
        for i in range(minidx - 1, -1, -1):
            # For case 17860, we can see that first 6 can be swapped with 1
            # but 8 can also be swapped with 7. So we cannot terminate when 6 is swapped with 1
            if digits[minidx] > digits[i] and i > swap_idx[1]:
                swap_idx[0], swap_idx[1], swap_idx[2] = True, i, minidx

        minidx -= 1

    can_swap = swap_idx[0]
    sort = True
    if can_swap:
        digits[swap_idx[1]], digits[swap_idx[2]] = digits[swap_idx[2]], digits[swap_idx[1]]
    else:
        # We couldn't swap. This means that we have numbers like
        # 4321 or 8000
        # Corner Case 1: 8000
        if is_number_thousands(digits):
            digits.append(0)
            sort = False
        else:
            minidx = find_non_zero_idx(digits)
            # Take the first non-zero value from the end (eg. 77430)
            digits[0], digits[minidx] = digits[minidx], digits[0]
            # Insert 0 at the 2nd location
            digits.insert(1, 0)
            swap_idx[1] = 1  # Start the sort from the 2nd position

    if sort is True:
        sort_idx = swap_idx[1]
        digits[sort_idx+1:] = sorted(digits[sort_idx+1:])

    num = create_number(digits)
    return num

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.replace("\n", "")
        new_num = find_following_integer(test)
        print(new_num)

import unittest

class UnitTests(unittest.TestCase):
    def testNextNumber(self):
        self.assertEqual(find_following_integer("727827"), 727872)
        self.assertEqual(find_following_integer("53799"), 53979)
        self.assertEqual(find_following_integer("41"), 104)
        self.assertEqual(find_following_integer("555147"), 555174)
        self.assertEqual(find_following_integer("98109"), 98190)
        self.assertEqual(find_following_integer("39352"), 39523)
        self.assertEqual(find_following_integer("1984"), 4189)
        self.assertEqual(find_following_integer("2000"), 20000)
        self.assertEqual(find_following_integer("99582"), 99825)
        self.assertEqual(find_following_integer("853770"), 857037)
        self.assertEqual(find_following_integer("59"), 95)
        self.assertEqual(find_following_integer("37"), 73)
        self.assertEqual(find_following_integer("78"), 87)
        self.assertEqual(find_following_integer("20189"), 20198)
        self.assertEqual(find_following_integer("166347"), 166374)
        self.assertEqual(find_following_integer("77787"), 77877)
        self.assertEqual(find_following_integer("800639"), 800693)
        self.assertEqual(find_following_integer("51756"), 51765)
        self.assertEqual(find_following_integer("71"), 107)
        self.assertEqual(find_following_integer("982818"), 982881)
        self.assertEqual(find_following_integer("539215"), 539251)
        self.assertEqual(find_following_integer("41"), 104)
        self.assertEqual(find_following_integer("1776"), 6177)
        self.assertEqual(find_following_integer("1"), 10)
        self.assertEqual(find_following_integer("163636"), 163663)
        self.assertEqual(find_following_integer("53"), 305)
        self.assertEqual(find_following_integer("464577"), 464757)
        self.assertEqual(find_following_integer("493977"), 497379)
        self.assertEqual(find_following_integer("86"), 608)
        self.assertEqual(find_following_integer("33417"), 33471)
        self.assertEqual(find_following_integer("137720"), 170237)
        self.assertEqual(find_following_integer("331519"), 331591)
        self.assertEqual(find_following_integer("385558"), 385585)
        self.assertEqual(find_following_integer("876181"), 876811)
        self.assertEqual(find_following_integer("61837"), 61873)
        self.assertEqual(find_following_integer("66664"), 406666)
        self.assertEqual(find_following_integer("7"), 70)
        self.assertEqual(find_following_integer("737773"), 773377)
        self.assertEqual(find_following_integer("253036"), 253063)
        self.assertEqual(find_following_integer("100"), 1000)
        self.assertEqual(find_following_integer("23"), 32)
        self.assertEqual(find_following_integer("83510"), 85013)
        self.assertEqual(find_following_integer("45"), 54)
        self.assertEqual(find_following_integer("9"), 90)
        self.assertEqual(find_following_integer("39811"), 81139)
        self.assertEqual(find_following_integer("1"), 10)
        self.assertEqual(find_following_integer("69470"), 69704)
        self.assertEqual(find_following_integer("923647"), 923674)
        self.assertEqual(find_following_integer("38"), 83)
        self.assertEqual(find_following_integer("76"), 607)
        self.assertEqual(find_following_integer("2000"), 20000)
        self.assertEqual(find_following_integer("869940"), 890469)
        self.assertEqual(find_following_integer("83"), 308)
        self.assertEqual(find_following_integer("23328"), 23382)
        self.assertEqual(find_following_integer("41"), 104)
        self.assertEqual(find_following_integer("731962"), 732169)
        self.assertEqual(find_following_integer("65555"), 505556)
        self.assertEqual(find_following_integer("698087"), 698708)
        self.assertEqual(find_following_integer("883614"), 883641)
        self.assertEqual(find_following_integer("161298"), 161829)
        self.assertEqual(find_following_integer("26"), 62)
        self.assertEqual(find_following_integer("2517"), 2571)
        self.assertEqual(find_following_integer("86"), 608)
        self.assertEqual(find_following_integer("17860"), 18067)
        self.assertEqual(find_following_integer("428244"), 428424)
        self.assertEqual(find_following_integer("611132"), 611213)
        self.assertEqual(find_following_integer("56"), 65)
        self.assertEqual(find_following_integer("33"), 303)
        self.assertEqual(find_following_integer("698457"), 698475)
        self.assertEqual(find_following_integer("862598"), 862859)
        self.assertEqual(find_following_integer("882712"), 882721)
        self.assertEqual(find_following_integer("431548"), 431584)
        self.assertEqual(find_following_integer("721151"), 721511)
        self.assertEqual(find_following_integer("71653"), 73156)
        self.assertEqual(find_following_integer("51049"), 51094)
        self.assertEqual(find_following_integer("653133"), 653313)
        self.assertEqual(find_following_integer("20698"), 20869)
        self.assertEqual(find_following_integer("77430"), 300477)
        self.assertEqual(find_following_integer("6811"), 8116)
        self.assertEqual(find_following_integer("19"), 91)
        self.assertEqual(find_following_integer("52"), 205)


if __name__ == "__main__":
    unittest.main()