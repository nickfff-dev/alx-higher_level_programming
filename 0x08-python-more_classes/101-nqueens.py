#!/usr/bin/python3
"""Solve the N queens problem using backtracking.
"""
import sys


def solve_n_queens(n):
    """Solve the N queens problem using backtracking.

    Args:
        n (int): The number of queens and the size of the chess board.

    Returns:
        list of list of int: A list of all solutions. Each solution
        is represented
            as a list of integers where the value of i-th integer
            represents the column
            number of the queen placed in the i-th row.
    """

    """Check if a queen can be placed at a given position.
    """
    def can_place(pos, ocuppied_positions):
        """Check if a queen can be placed at a given position.

        Args:
            pos (int): The column number of the new queen.
            ocuppied_positions (list of int): The column numbers of the
            already placed queens.

        Returns:
            bool: True if a queen can be placed at the given position,
            False otherwise.
        """
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
                (ocuppied_positions[i] - i == pos - len(ocuppied_positions)) \
                    or (ocuppied_positions[i] + i ==
                        pos + len(ocuppied_positions)):
                return False
        return True

    """Place queens one by one in different columns.
    """

    def place_queens(n, index, ocuppied_positions, all_solutions):
        """Place queens one by one in different columns.

        Args:
            n (int): The number of queens and the size of the chess board.
            index (int): The index of the current queen to place.
            ocuppied_positions (list of int): The column numbers of
            the already placed queens.
            all_solutions (list of list of int): A list of all solutions
            found so far.
        """
        if index == n:
            all_solutions.append(ocuppied_positions[:])
            return

        for i in range(n):
            if can_place(i, ocuppied_positions):
                ocuppied_positions.append(i)
                place_queens(n, index + 1, ocuppied_positions, all_solutions)
                ocuppied_positions.pop()

    all_solutions = []
    place_queens(n, 0, [], all_solutions)
    return all_solutions


"""Print the solutions to the N queens problem.
"""


def print_solutions(solutions):
    """Print the solutions to the N queens problem.

    Args:
        solutions (list of list of int): The solutions to the N queens problem.
    """
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


"""The main function of the program.
"""


def main():
    """The main function of the program.

    Handles the command-line arguments and prints the solutions to the N
    queens problem.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
