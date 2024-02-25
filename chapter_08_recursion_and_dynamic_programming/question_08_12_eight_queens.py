from typing import List


GRID_SIZE = 8


def check_valid(columns: List[int], row1: int, col1: int) -> bool:
    for row2 in range(row1):
        col2 = columns[row2]
        # Check if row1 and row1 have queens in the same colums
        if col1 == col2:
            return False

        # Check diagonals: If the distance between the columns equal the distance between the rows. Then, they are on
        # the same diagonal.
        row_d = row1 - row2  # row1 > row2 as per recursion call, so no need to use abs.
        col_d = abs(col1 - col2)
        if row_d == col_d:
            return False

    return True


def place_queens(row: int, columns: List[int], results: List[List[int]]) -> None:
    if row == GRID_SIZE:  # Found valid placement
        results.append(columns.copy())
    else:
        for col in range(GRID_SIZE):
            if check_valid(columns, row, col):
                columns[row] = col  # Place queen
                place_queens(row + 1, columns, results)

