from enum import Enum, auto
from random import randrange
from typing import List


class AutoName(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self


class Color(AutoName):
    Black = auto()
    White = auto()
    Red = auto()
    Yellow = auto()
    Green = auto()

    def __str__(self):
        return self.name[0]


def print_screen(screen:List[List[Color]]) -> None:  # noqa
    for row in screen:
        for color in row:
            print(color, end='')
        print()


def paint_fill(screen: List[List[Color]], row: int, col: int, n_color: Color) -> None:  # noqa
    if screen[row][col] is n_color:
        return None
    r_paint_fill(screen, row, col, screen[row][col], n_color)


def r_paint_fill(screen: List[List[Color]], row: int, col: int, o_color: Color, n_color: Color) -> None:  # noqa
    if row < 0 or row >= len(screen) or col < 0 or col >= len(screen[0]):
        return None

    if screen[row][col] is o_color:
        screen[row][col] = n_color
        r_paint_fill(screen, row - 1, col, o_color, n_color)
        r_paint_fill(screen, row + 1, col, o_color, n_color)
        r_paint_fill(screen, col - 1, col, o_color, n_color)
        r_paint_fill(screen, col + 1, col, o_color, n_color)


if __name__ == "__main__":
    N = 10
    screen = [[Color.Black] * 10 for _ in range(10)]
    for _ in range(100):
        screen[randrange(10)][randrange(10)] = Color.Green
    print_screen(screen)
    paint_fill(screen, 3, 3, Color.White)
    print()
    print_screen(screen)
