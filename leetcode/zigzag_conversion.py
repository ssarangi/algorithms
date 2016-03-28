class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = [""] * numRows
        center = numRows // 2
        cp = 0
        column = 0
        terminate = False
        while not terminate:
            if column % 2 == 0:
                for i in range(0, numRows):
                    arr[i] += s[cp]
                    cp += 1
                    if cp >= len(s):
                        terminate = True
                        break
            else:
                arr[center] += s[cp]
                cp += 1
                if cp >= len(s):
                    terminate = True

            column += 1

        final = ""
        for i in arr:
            final += i

        return final

soln = Solution()

s = "PAYPALISHIRING"
numRows = 3
print(soln.convert(s, numRows))
