def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    # Check the same column above the current row
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_backtraking(board, row, n):
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_backtraking(board, row + 1, n)
            board[row][col] = 0

    return False

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    # Place the first queen at the top-left corner (arbitrary)
    board[0][0] = 1

    if solve_backtraking(board, 1, n):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists for this configuration.")

n = 4
solve_nqueens(4)
