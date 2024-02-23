from __future__ import annotations

from collections import deque
from typing import Optional


class Tower:
    def __init__(self, name=None):
        self.name = name
        self.disks = None  # type: Optional[deque]

    def add(self, disk: int) -> None:
        if not self.disks:
            self.disks = deque()
        elif self.disks and self.disks[-1] < disk:
            raise Exception('Cannot place disk')
        self.disks.append(disk)

    def print(self):
        print(f'Content of Tower {self.name}: {list(self.disks)}')

    def move_top_to(self, destination: Tower) -> None:  # noqa
        destination.add(self.disks.pop())

    def move_disks(self, number_of_disks: int, destination: Tower, buffer: Tower) -> None:  # noqa
        if number_of_disks <= 0:
            return None

        self.move_disks(number_of_disks - 1, buffer, destination)
        self.move_top_to(destination)
        buffer.move_disks(number_of_disks - 1, destination, self)


if __name__ == "__main__":
    source, buffer, destination = Tower('s'), Tower('b'), Tower('d')

    # Load up towers.
    number_of_disks = 5
    for d in range(number_of_disks - 1, -1, -1):
        source.add(d)

    source.print()
    source.move_disks(number_of_disks, destination, buffer)
    destination.print()
