#Implement n-queens problem using backtracking
def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, row, n):
    if row == n:
        print_board(board)
        return True
    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            res = solve_nqueens(board, row + 1, n) or res
            board[row][col] = 0
    return res
def n_queens(n):
    board = [[0] * n for _ in range(n)]
    if not solve_nqueens(board, 0, n):
        print("No solution exists.")
n = int(input("Enter number of queens: "))
n_queens(n)
