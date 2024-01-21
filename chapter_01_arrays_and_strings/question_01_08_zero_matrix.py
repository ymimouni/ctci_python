"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O.
Hints: # 17, #74, #102
"""

import unittest
import copy
from ctci.ctci_library import assorted


def zero_matrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix

    m = len(matrix)
    n = len(matrix[0])

    matrix_copy = copy.deepcopy(matrix)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                nullify_row(matrix_copy, i)
                nullify_column(matrix_copy, j)

    return matrix_copy


# No extra space.
def zero_matrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix

    m = len(matrix)
    n = len(matrix[0])

    row_has_zero = False
    column_has_zero = False

    # Check if first row has zero.
    for j in range(n):
        if matrix[0][j] == 0:
            row_has_zero = True

    # Check if first column has zero.
    for i in range(m):
        if matrix[i][0] == 0:
            column_has_zero = True

    # Check for zeros in the rest of the array.
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Nullify rows based on values in first column.
    for i in range(1, m):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)

    # Nullify columns based on values in first row.
    for j in range(1, n):
        if matrix[0][j] == 0:
            nullify_column(matrix, j)

    # Nullify first row
    if row_has_zero:
        nullify_row(matrix, 0)

    # Nullify first column
    if column_has_zero:
        nullify_column(matrix, 0)

    # assorted_methods.print_matrix(matrix)

    return matrix


def nullify_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def nullify_column(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = 0


class Test(unittest.TestCase):
    """Test Cases"""
    data = [
        ([
             [1, 2, 3, 4, 0],
             [6, 0, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 0, 18, 19, 20],
             [21, 22, 23, 24, 25]
         ], [
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [11, 0, 13, 14, 0],
             [0, 0, 0, 0, 0],
             [21, 0, 23, 24, 0]
         ])
    ]

    def test_zero_matrix(self):
        for matrix, expected in self.data:
            self.assertEqual(expected, zero_matrix(matrix))


if __name__ == "__main__":
    unittest.main()
