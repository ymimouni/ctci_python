"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
Hints: #51, #100
"""

import unittest


# def rotate_matrix(matrix):
#     if len(matrix) == 0 or len(matrix) != len(matrix[0]):
#         return False  # Not a square
#     n = len(matrix)
#
#     for layer in range(int(n / 2)):
#         first = layer
#         last = n - 1 - layer
#         for i in range(layer, int(n - 1 - layer)):
#             offset = i - first
#             # Save top
#             temp = matrix[first][i]
#             # left -> top
#             matrix[first][i] = matrix[last - offset][first]
#             # bottom -> left
#             matrix[last - offset][first] = matrix[last][last - offset]
#             # right -> bottom
#             matrix[last][last - offset] = matrix[i][last]
#             # temp -> Right
#             matrix[i][last] = temp
#
#     return matrix


def rotate_matrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False  # Not a square
    n = len(matrix[0])

    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            # Save matrix[i][j]
            temp = matrix[i][j]
            # left -> top
            matrix[i][j] = matrix[n - 1 - j][i]
            # bottom -> left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            # right -> bottom
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            # top -> right
            matrix[j][n - 1 - i] = temp

    return matrix


class Test(unittest.TestCase):
    """Test cases."""
    data = [
        ([
             [1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]
         ], [
             [21, 16, 11, 6, 1],
             [22, 17, 12, 7, 2],
             [23, 18, 13, 8, 3],
             [24, 19, 14, 9, 4],
             [25, 20, 15, 10, 5]
         ])
    ]

    def test_rotate_matrix(self):
        for matrix, expected in self.data:
            self.assertEqual(expected, rotate_matrix(matrix))


if __name__ == "__main__":
    unittest.main()
