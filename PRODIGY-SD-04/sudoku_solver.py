# Prodigy Infotech Internship - Task 04
# Sudoku Solver using Backtracking Algorithm (User Input Version)

def print_board(board):
    """Display the Sudoku board in a formatted grid."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    """Find the next empty cell (represented by 0)."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j  # row, col
    return None

def is_valid(board, num, pos):
    """Check if placing num at pos (row, col) is valid."""
    row, col = pos

    # Check row
    for j in range(9):
        if board[row][j] == num and j != col:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    # Check 3x3 grid
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    """Solve the Sudoku board using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True  # Solved
    else:
        row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Reset (backtrack)

    return False

def get_user_input():
    """Takes Sudoku grid input from the user."""
    print("Enter your Sudoku puzzle row by row (use 0 for empty cells):")
    board = []
    for i in range(9):
        while True:
            try:
                row = input(f"Row {i+1}: ").strip()
                nums = [int(x) for x in row.split()]
                if len(nums) == 9:
                    board.append(nums)
                    break
                else:
                    print("⚠️ Please enter exactly 9 numbers separated by spaces.")
            except ValueError:
                print("⚠️ Invalid input. Please enter numbers only.")
    return board


if __name__ == "__main__":
    print("🧩 Sudoku Solver ")
    print("-----------------------------------------\n")

    sudoku_board = get_user_input()

    print("\n🧩 Unsolved Sudoku Puzzle:")
    print_board(sudoku_board)

    print("\nSolving...\n")

    if solve(sudoku_board):
        print("✅ Solved Sudoku Puzzle:")
        print_board(sudoku_board)
    else:
        print("❌ No solution exists for this puzzle.")
