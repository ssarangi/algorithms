# https://leetcode.com/problems/dungeon-game/

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        class Room:
            def __init__(self, row, col):
                self.row = row
                self.col = col

            def __eq__(self, other):
                return self.row == other.row and self.col == other.col

            def __str__(self):
                return str(self.row) + " - " + str(self.col)

        def calculate(dungeon, curr_pt, end_pt, health):
            curr_health = health + dungeon[curr_pt.row][curr_pt.col]
            if curr_pt == end_pt:
                return curr_health

            curr_check_val = min(curr_health, 0)

            down = 0
            if curr_pt.row + 1 <= end_pt.row:
                down = calculate(dungeon, Room(curr_pt.row + 1, curr_pt.col), end_pt, curr_health)

            right = 0
            if curr_pt.col + 1 <= end_pt.col:
                right = calculate(dungeon, Room(curr_pt.row, curr_pt.col + 1), end_pt, curr_health)

            return min(curr_check_val, down, right)


        end_pt = Room(len(dungeon) - 1, len(dungeon[0]) - 1)
        start_pt = Room(0, 0)

        health = calculate(dungeon, start_pt, end_pt, 0)
        return health

soln = Solution()
dungeon = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]

print(soln.calculateMinimumHP(dungeon))