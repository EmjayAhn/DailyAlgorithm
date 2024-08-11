def is_safe(board, row, col, N):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_nqueens_util(board, col + 1, N):
                return True
            board[i][col] = 0  # Backtrack

    return False

def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens_util(board, 0, N):
        print("Solution does not exist")
        return False

    print_board(board)
    return True

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))

# Example usage:
N = 8
solve_nqueens(N)