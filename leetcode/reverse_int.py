class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        arr = []
        negative = x < 0
        x = abs(x)

        while x > 0:
            arr.append(x % 10)
            x = x // 10

        reversed_num = 0
        for i in range(len(arr) - 1, -1, -1):
            reversed_num += arr[i] * (10 ** (len(arr) - 1 - i))

        if reversed_num > 0x7FFFFFFF:
            # Overflow happened. We need to return 0
            return 0

        if negative:
            reversed_num *= -1

        return reversed_num

soln = Solution()
x = 321

print(soln.reverse(x))
