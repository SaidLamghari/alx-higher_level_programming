#!/usr/bin/python3
"""program that solves the N queens problem"""


import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at the given position on the board.
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n, solutions):
    """
    Solve the N-queens problem using backtracking.
    """
    if col == n:
        # Found a solution, add it to the list of solutions
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_n_queens_util(board, col + 1, n, solutions)

            # Backtrack and remove the queen from the current position
            board[i][col] = 0

    return False


def solve_n_queens(n):
    """
    Solve the N-queens problem and print the solutions.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    if not solve_n_queens_util(board, 0, n, solutions):
        print("No solution found.")
        return

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number.")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4.")
        sys.exit(1)

    solve_n_queens(n)
