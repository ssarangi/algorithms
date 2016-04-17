def valid_row(board, row):
    seen = 0
    for col in range(0, len(board[row])):
        if board[row][col] is None:
            continue
        
        if seen & (1 << board[row][col]):
            return False
        else:
            seen |= (1 << board[row][col])
            
    return True

def valid_column(board, col):
    seen = 0
    for row in range(0, len(board)):
        if board[row][col] is None:
            continue

        if seen & (1 << board[row][col]):
            return False
        else:
            seen |= (1 << board[row][col])

    return True

def valid_subboard(board, i, j, size_x, size_y):
    seen = 0
    for row in range(i, i + size_y):
        for col in range(j, j + size_x):
            if board[row][col] is None:
                continue

            if seen & (1 << board[row][col]):
                return False
            else:
                seen |= (1 << board[row][col])

    return True

def is_valid_sudoku(board):
    valid = True
    for i in range(len(board)):
        valid &= valid_row(board, i)
        if valid is False:
            return False
        
    for i in range(len(board[0])):
        valid &= valid_column(board, i)
        if valid is False:
            return False
        
    for i in range(0, len(board), 3):
        for j in range(0, len(board[0]), 3):
            valid &= valid_subboard(board, i, j, 3, 3)
            if valid is False:
                return False
                
    return True

board = [
    [5, 3, None, None, 7, None, None, None, None],
    [6, None, None, 1, 9, 5, None, None, None],
    [None, 9, 8, None, None, None, None, 6, None],
    [8, None, None, None, 6, None, None, None, 3],
    [4, None, None, 8, None, 3, None, None, 1],
    [7, None, None, None, 2, None, None, None, 6],
    [None, 6, None, None, None, None, 2, 8, None],
    [None, None, None, 4, 1, 9, None, None, 5],
    [None, None, None, None, 8, None, None, 7, 9]
]

print(is_valid_sudoku(board))