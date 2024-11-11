print("Enter the number of queens: ")
N = int(input())
board = [[0] * N for _ in range(N)]

def is_attack(i, j):
    # Check if there's a queen in the same column
    for k in range(i):
        if board[k][j] == 1:
            return True

    # Check upper-left diagonal
    row, col = i, j
    while row >= 0 and col >= 0:
        if board[row][col] == 1:
            return True
        row -= 1
        col -= 1

    # Check upper-right diagonal
    row, col = i, j
    while row >= 0 and col < N:
        if board[row][col] == 1:
            return True
        row -= 1
        col += 1  # Move right

    return False

def n_queen(row):
    # If all queens are placed successfully
    if row == N:
        return True

    # Try placing the queen in each column of the current row
    for j in range(N):
        if not is_attack(row, j):
            board[row][j] = 1  # Place the queen

            # Recursively attempt to place queens in the next row
            if n_queen(row + 1):
                return True

            board[row][j] = 0  # Backtrack

    return False

# Start solving the N-Queens problem
if n_queen(0):
    # Print the solution (board configuration)
    for row in board:
        print(row)
else:
    print("No solution")
