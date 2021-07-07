""" An algorithm to solve sudoku puzzles using backtracking. """

__author__ = "Kim Yen Pham"


"""
PLAN FOR ALGORITHM:
1.  find an empty spot
2.  make a guess
3.  check the row, column and box if it is valid
        if not, make another guess
        if it is, place the guess and exit the loop
4.  find another empty spot
5.  repeat until there are no more empty spots OR until all
    possible guesses have been made
        if all possible guesses have been made, backtrack
"""


def get_grid_size(size) -> int:
    """ Returns the size of the grid (square/box) when given the length of the sudoku puzzle."""
    return int(size ** 0.5)


def print_sudo(sudo, size) -> None:
    """ Helper function to display the sudoku puzzle in a more readable way. """
    grid_size = get_grid_size(size)
    if grid_size == 3:  # sudoku size is 9x9
        hori_border = '--------'
    else:  # if grid size is 2 aka sudoku size is 4x4
        hori_border = '------'

    print(hori_border*grid_size)  # prints top border
    for row in range(size):
        for col in range(size):
            # prints vertical borders (excluding rightmost border)
            if col % grid_size == 0:
                print("|", end=' ')

            if sudo[row][col] == 0:  # prints '-' to represent empty spots for clarity
                print("-", end=' ')
            else:
                print(sudo[row][col], end=' ')  # prints the numbers

            if col == size-1:  # prints rightmost vertical border
                print("|", end=' ')
                if (row+1) % grid_size != 0:
                    print()
        if (row+1) % grid_size == 0:
            print()
            print(hori_border*grid_size)


def find_empty(sudo, size) -> tuple:
    """ Finds and returns the next empty position in the sudoku puzzle, where an empty spot is indicated by the
    integer 0, and where the position represented by its row and column.
    """
    for row in range(size):
        for column in range(size):
            if sudo[row][column] == 0:
                return row, column
    return None, None


def check_valid(guess, row, col, sudo, size) -> bool:
    """ Checks if the given guess is valid in the given position according to the rules of sudoku. Returns True if the
    guess is valid, False otherwise.
    To be a valid guess, the guess must not already be in the same row, same column, or in the same box of the sudoku
    grid (ie. if the guess is made, it should not appear more than once in the row, column or grid).
    """
    print("checking")

    def check_row() -> bool:
        """ Returns True is the guess is not in the given row. False otherwise."""
        if guess in sudo[row]:
            return False
        return True

    def check_column() -> bool:
        """ Returns True is the guess is not in the given column. False otherwise."""
        for rows in range(size):
            if sudo[rows][col] == guess:
                return False
        return True

    def check_square() -> bool:
        """ Returns True is the guess is not in the given grid. False otherwise."""
        grid_size = get_grid_size(size)
        row_start = (row // grid_size) * grid_size
        col_start = (col // grid_size) * grid_size
        for rows in range(int(row_start), int(row_start + grid_size)):
            for cols in range(int(col_start), int(col_start + grid_size)):
                if sudo[rows][cols] == guess:
                    return False
        return True

    return check_row() and check_column() and check_square()


def solve(sudo, size):
    row, col = find_empty(sudo, size)

    print(f"position: {row, col}")

    if row is None:
        print("done!")
        #print_sudo(sudo, size)
        return True

    else:  # if empty, change it to 1)

        for guess in range(1, size+1):
            print(f"guess: {guess}")
            if check_valid(guess, row, col, sudo, size):
                sudo[row][col] = guess
                print(f"changed to {guess}")
                print("valid so find next")
                if solve(sudo, size):
                    return True
            print("backtracked")
            sudo[row][col] = 0
        return False


if __name__ == '__main__':
    grid = [[0, 1], [0, 0]]

    sudo2 = [[1, 1],
             [0, 1]]

    sudo4 = [[0, 2, 3, 0],
             [1, 4, 2, 3],
             [3, 0, 0, 2],
             [2, 3, 0, 4]]

    sudo9 = [[0, 0, 0, 9, 1, 0, 4, 0, 7],
             [3, 0, 4, 6, 8, 0, 0, 1, 0],
             [0, 7, 9, 0, 5, 0, 6, 0, 3],
             [9, 0, 2, 0, 0, 0, 8, 0, 1],
             [0, 1, 5, 0, 0, 6, 3, 4, 0],
             [0, 3, 0, 0, 9, 0, 0, 5, 0],
             [2, 0, 0, 5, 3, 0, 7, 0, 0],
             [0, 0, 3, 1, 0, 0, 0, 9, 0],
             [6, 0, 0, 4, 7, 0, 1, 3, 0], ]
    # print(solve(sudo2,2))
    # print(sudo2)
    # solve(sudo4,4)
    # print(sudo4)
    #print(solve(sudo4, 4))
    #print_sudo(sudo4, 4)
    print(solve(sudo9, 9))
    print_sudo(sudo9, 9)
