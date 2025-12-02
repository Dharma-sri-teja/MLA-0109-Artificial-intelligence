# 8 Queens problem using Backtracking

N = 8  # Chess board size (8x8)

# Function to print the board
def print_solution(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

# Check if placing queen at board[row][col] is safe
def is_safe(board, row, col):
    # Check column
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
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Backtracking function to solve
def solve(board, row):
    # If all queens placed successfully
    if row == N:
        print("Solution Found:")
        print_solution(board)
        return True

    # Try placing queen in all columns of current row
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            if solve(board, row + 1):  # Move to next row
                return True
            board[row][col] = 0  # Backtrack

    return False

# Main program
board = [[0 for _ in range(N)] for _ in range(N)]

if not solve(board, 0):
    print("No solution exists")
