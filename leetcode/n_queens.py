import unittest

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def valid_queen_pos(board, row, col):
            n = len(board)
            
            if board[row][col] == 1:
                return False
                
            for i in range(0, n):
                if i != row and board[i][col] == 1:
                    return False
                    
            for i in range(0, n):
                if i != col and board[row][i] == 1:
                    return False
            
            cr = 0
            cc = 0
            while cr != n and cc != n:
                if cr != row and cc != col:
                    if board[cr][cc] == 1:
                        return False
                        
                cr += 1
                cc += 1

            cr = 0
            cc = n - 1
            while cr != n and cc != n:
                if cr != row and cc != col:
                    if board[cr][cc] == 1:
                        return False
                        
                cr += 1
                cc += 1
                        
            return True


        def get_string_repr(board):
            board_str = []
            for row in range(0, n):
                s = ""
                for col in range(0, n):
                    if board[row][col] == 1:
                        s += "Q"
                    else:
                        s += "."
                board_str.append(s)
                
            return board_str
        
        def solve(n, nq, board, results):
            if nq == 0:
                results.append(board)
                return True
            
            found_soln = False
            for row in range(0, n):
                for col in range(0, n):
                    if valid_queen_pos(board, row, col):
                        board[row][col] = 1
                        res = solve(n , nq - 1, board, results)
                        if res == False:
                            board[row][col] = 0
                        found_soln |= res
            
            return found_soln
        
        results = []
        boards = []
        board = [[0 for _ in range(0, n)] for _ in range(0, n)]
        solve(n, n, board, boards)
        for b in boards:
            board_str = get_string_repr(board)
            results.append(board_str)
                
        return results
    
    
class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testIsNumber(self):
        self.assertEqual(self.soln.solveNQueens(4), 
        [
             [".Q..",  # Solution 1
              "...Q",
              "Q...",
              "..Q."],
            
             ["..Q.",  # Solution 2
              "Q...",
              "...Q",
              ".Q.."]
        ])

if __name__ == "__main__":
    unittest.main()