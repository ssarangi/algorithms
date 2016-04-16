# Based on https://www.youtube.com/watch?v=RORuwHiblPc&index=18&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

import sys

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        matrix = [[0] * len(words) for _ in range(0, len(words))]

        lengths = {}
        for word in words:
            lengths[word] = len(word)

        num_words = len(words)
        # Create the matrix for the costs of each line
        for i in range(0, num_words):
            for j in range(i, num_words):
                num_spaces = j - i

                # Count the total length of the words
                total_len = num_spaces
                for k in range(i, j+1):
                    total_len += lengths[words[k]]

                if total_len > maxWidth:
                    space_left = "inf"
                else:
                    space_left = (maxWidth - total_len) * (maxWidth - total_len)

                matrix[i][j] = space_left

        # Now create 2 arrays of the same lengths as the num words.
        # One array will store the costs of breaking a line and one array
        # will store where the break actually happened.
        min_break_cost = [0] * num_words
        break_points = [0] * num_words

        i = num_words - 1

        while i >= 0:
            j = num_words - 1

            if matrix[i][j] != "inf":
                min_break_cost[i] = matrix[i][j]
                break_points[i] = j + 1
                i -= 1
            else:
                # Split at j - 1
                split = j - 1
                minv = sys.maxsize
                min_split_pt = -1
                while split > i:
                    if matrix[i][split] == "inf":
                        continue

                    split -= 1
                    cost = matrix[i][split]
                    total_cost = cost + min_break_cost[j]
                    if minv > total_cost:
                        minv = total_cost
                        min_split_pt = j

                min_break_cost[i] = min_split_pt
                break_points[i] = j

soln = Solution()

#words = ["This", "is", "an", "example", "of", "text", "justification."]
#L = 16

words = ["tushar", "roy", "likes", "to", "code"]
L = 10

print(soln.fullJustify(words, L))