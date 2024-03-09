from dataclasses import dataclass
from typing import List, Tuple, Optional

from ctci.ctci_library.assorted import unique_pairs


# def find_element(matrix: List[List[Optional[int]]], e: int) -> Optional[Tuple[int, int]]:  # noqa
#     row, col = 0, len(matrix[0]) - 1  # noqa
#     while row < len(matrix) and col >= 0:
#         if matrix[row][col] == e:
#             return row, col
#         elif matrix[row][col] > e:
#             col -= 1
#         else:
#             row += 1
#
#     return None


@dataclass
class Coordinates:
    row: int
    column: int

    def clone(self):
        return Coordinates(self.row, self.column)

    def is_before(self, p):
        return self.row <= p.row and self.column <= p.column

    def set_average(self, min, max):  # noqa
        self.row = int((min.row + max.row) / 2)
        self.column = int((min.column + max.column) / 2)

    def in_bounds(self, matrix):  # noqa
        return 0 <= self.row < len(matrix) and 0 <= self.column < len(matrix[0])


def find_element(matrix: List[List[Optional[int]]], e: int):  # noqa
    origin, dest = Coordinates(0, 0), Coordinates(len(matrix) - 1, len(matrix[0]) - 1)
    return r_find_element(matrix, e, origin, dest)


def r_find_element(matrix: List[List[Optional[int]]], e: int, origin: Coordinates, dest: Coordinates):  # noqa
    if not origin.in_bounds(matrix) or not dest.in_bounds(matrix):
        return None

    if matrix[origin.row][origin.column] == e:
        return origin
    elif not origin.is_before(dest):
        return None

    # Set start to origin and end to the end of the diagonal. Since the grid may not be square, the end of the
    # diagonal may be different than dest.
    start = origin.clone()
    diag_distance = min(dest.row - origin.row, dest.column - origin.column)
    end = Coordinates(start.row + diag_distance, start.column + diag_distance)
    p = Coordinates(0, 0)

    # Do binary search on the diagonal, looking for the first element greated than x.
    while start.is_before(end):
        p.set_average(start, end)
        if e > matrix[p.row][p.column]:
            start.row = p.row + 1
            start.column = p.column + 1
        else:
            end.row = p.row - 1
            end.column = p.column - 1

    # Split the grid into quadrants. Search the bottom left and the top right.
    return partition_and_search(matrix, e, origin, dest, start)


def partition_and_search(matrix: List[List[Optional[int]]], e: int, origin: Coordinates, dest: Coordinates,  # noqa
                         pivot: Coordinates):
    lower_left_origin = Coordinates(pivot.row, origin.column)
    lower_left_dest = Coordinates(dest.row, pivot.column - 1)
    upper_right_origin = Coordinates(origin.row, pivot.column)
    upper_right_dest = Coordinates(pivot.row - 1, dest.column)

    lower_left = r_find_element(matrix, e, lower_left_origin, lower_left_dest)
    if not lower_left:
        return r_find_element(matrix, e, upper_right_origin, upper_right_dest)

    return lower_left


if __name__ == "__main__":
    M = 5
    N = 5
    matrix = [[None] * N for _ in range(M)]

    for row, col in unique_pairs(M, N):
        matrix[row][col] = 10 * row + col

    for row, col in unique_pairs(M, M):
        e = 10 * row + col
        print('{e}: ', find_element(matrix, e))
