# 0 represents an empty cell

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def is_safe(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    r = (row // 3) * 3
    c = (col // 3) * 3

    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if board[i][j] == num:
                return False

    return True

def solve():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:

                # Constraint propagation
                for num in range(1, 10):
                    if is_safe(board, i, j, num):
                        board[i][j] = num

                        # Backtracking
                        if solve():
                            return True

                        board[i][j] = 0

                return False

    return True

if solve():
    print("Sudoku Solution:")
    for row in board:
        print(row)
else:
    print("No solution exists")