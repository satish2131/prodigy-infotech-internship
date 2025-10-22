# Prodigy Infotech Internship - Task 04  
## Sudoku Solver (Python)

### 🎯 Objective
Create a Python program that takes a **Sudoku puzzle as user input** and automatically solves it using the **Backtracking Algorithm**.

---

### ⚙️ Features
- Takes **user input** (9 rows of 9 numbers each)
- Accepts **0 for empty cells**
- Automatically solves using recursion & backtracking
- Displays both the **unsolved** and **solved** Sudoku grids

---

### 🧩 How to Run

1. Open **Command Prompt**:
   ```bash
   cd "D:\satish\prodigy intern\SD\PRODIGY-SD-04"
   python sudoku_solver.py
Enter Sudoku rows when prompted.
Each row must have 9 integers (use 0 for blanks).

Example:

sql
Copy code
Row 1: 7 8 0 4 0 0 1 2 0
Row 2: 6 0 0 0 7 5 0 0 9
...
Row 9: 0 4 9 2 0 6 0 0 7
The program displays:

The Unsolved Sudoku

The Solved Sudoku

🧠 Algorithm Used
Backtracking Algorithm

Steps:

Find the first empty cell (0).

Try numbers 1–9.

Check if valid (row, column, box).

Recursively continue.

If no valid number fits, backtrack and try again.

🧮 Example Input 
7 8 0 4 0 0 1 2 0
6 0 0 0 7 5 0 0 9
0 0 0 6 0 1 0 7 8
0 0 7 0 4 0 2 6 0
0 0 1 0 5 0 9 3 0
9 0 4 0 6 0 0 0 5
0 7 0 3 0 0 0 1 2
1 2 0 0 0 7 4 0 0
0 4 9 2 0 6 0 0 7
