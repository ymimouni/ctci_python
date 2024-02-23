from dataclasses import dataclass
from typing import Optional, List, Set


@dataclass(eq=True, frozen=True)
class Point:
    row: int
    column: int


def get_path(grid: List[List]) -> Optional[List[Point]]:
    if not grid or not len(grid):
        return None
    path = []  # type: List[Point]
    failed_points = set()
    if r_get_path(grid, len(grid) - 1, len(grid[0]) - 1, path, failed_points):
        return path
    return None


def r_get_path(grid: List[List], row: int, col: int, path: List, failed_points: Set) -> bool:
    # If out of bound or not available, return.
    if row < 0 or col < 0 or grid[row][col]:
        return False

    p = Point(row, col)

    if p in failed_points:
        return False

    is_at_origin = row == 0 and col == 0

    # If there is a path from the start to my current location, add my location
    if is_at_origin or r_get_path(grid, row - 1, col, path, failed_points) or r_get_path(grid, row, col - 1, path,
                                                                                         failed_points):
        path.append(p)
        return True

    failed_points.add(p)
    return False


def test_get_path():
    grid = [[0, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 0]]
    assert get_path(grid) == [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3), Point(1, 3), Point(2, 3), Point(2, 4),
                              Point(2, 5), Point(2, 6), Point(3, 6)]

    grid = [[0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 0]]
    assert get_path(grid) is None


# import unittest
#
#
# def path_through_grid(grid):
#     if len(grid) == 0:
#         return []
#     search = []
#     for r, row in enumerate(grid):
#         search.append([])
#         for c, blocked in enumerate(row):
#             if r == 0 and c == 0:
#                 search[r].append("start")
#             elif blocked:
#                 search[r].append(None)
#             elif r > 0 and search[r - 1][c]:
#                 search[r].append("down")
#             elif c > 0 and search[r][c - 1]:
#                 search[r].append("right")
#             else:
#                 search[r].append(None)
#     path = ["end"]
#     r, c = len(grid) - 1, len(grid[0]) - 1
#     if not search[r][c]:
#         return None
#     while c > 0 or r > 0:
#         path.append(search[r][c])
#         if search[r][c] == "down":
#             r -= 1
#         else:
#             c -= 1
#     path.append("start")
#     path.reverse()
#     return path
#
#
# class Test(unittest.TestCase):
#     def test_path_through_grid(self):
#         grid = [[0, 0, 0, 0, 0, 1, 0],
#                 [0, 1, 1, 0, 1, 1, 0],
#                 [0, 0, 0, 0, 0, 0, 0],
#                 [1, 1, 0, 0, 0, 1, 0]]
#         self.assertEqual(path_through_grid(grid), ["start", "right", "right",
#                                                    "right", "down", "down", "right", "right", "right", "down", "end"])
#         grid = [[0, 0, 0, 0, 0, 0, 1],
#                 [0, 1, 0, 1, 1, 1, 0],
#                 [0, 0, 0, 1, 0, 0, 0],
#                 [1, 1, 0, 0, 0, 1, 0]]
#         self.assertEqual(path_through_grid(grid), None)
#
#
# if __name__ == "__main__":
#     unittest.main()
