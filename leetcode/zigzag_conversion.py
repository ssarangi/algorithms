class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0 or s == "" or numRows == 1:
            return s

        arr = [""] * numRows

        cp = 0
        current_row = 0
        row_change = 1
        while cp < len(s):
            arr[current_row] += s[cp]
            current_row += row_change

            if current_row == numRows - 1:
                row_change = -1
            elif current_row == 0:
                row_change = 1

            cp += 1

        final = ""
        for i in arr:
            final += i

        return final

soln = Solution()

s = "PAYPALISHIRING"
numRows = 3

s = "AB"
numRows = 1

print(soln.convert(s, numRows))
