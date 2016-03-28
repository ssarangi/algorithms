class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        def create_num(arr):
            INT_MAX = 2147483647
            INT_MIN = -2147483648

            num = 0
            for i in range(len(arr) - 1, -1, -1):
                num += arr[i] * (10 ** (len(arr) - 1 - i))

            if negative:
                num *= -1

            num = min(max(num, INT_MIN), INT_MAX)
            return num

        s = s.strip()

        if s == "" or len(s) == 0:
            return 0

        arr = []
        negative = False
        seen_sign = False
        for c in s:
            if c == "-" and not seen_sign:
                negative = True
                seen_sign = True
                continue
            elif c == "+" and not seen_sign:
                negative = False
                seen_sign = True
                continue
            elif c == " ":
                return create_num(arr)

            try:
                iv = int(c)
                arr.append(iv)
            except:
                return create_num(arr)

        return create_num(arr)


soln = Solution()

s = "123  456"
print(soln.myAtoi(s))
