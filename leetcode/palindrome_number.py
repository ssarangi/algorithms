class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        tmp = x
        num_digits = 0
        while tmp > 0:
            tmp = tmp // 10
            num_digits += 1

        p1 = num_digits - 1
        p2 = 1

        tmp1 = x
        tmp2 = x
        while p1 >= p2:
            d1 = tmp1 // (10 ** p1)
            tmp1 -= d1 * (10 ** p1)

            d2 = tmp2 % (10)
            tmp2 = tmp2 // 10

            if d1 != d2:
                return False

            p1 -= 1
            p2 += 1

        return True

soln = Solution()

x = 1221
print(soln.isPalindrome(x))
