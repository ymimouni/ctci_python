import sys
from typing import Tuple


def islice(iterable, *args):
    """An implementation of itertools.islice."""
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
    s = slice(*args)
    start, stop, step = s.start or 0, s.stop or sys.maxsize, s.step or 1
    it = iter(range(start, stop, step))
    try:
        nexti = next(it)
    except StopIteration:
        return
    try:
        for i, element in enumerate(iterable):
            if i == nexti:
                yield element
                nexti = next(it)
    except StopIteration:
        return


def print_matrix(matrix):
    """Pretty print a matrix."""
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_forward(self):
        if self.next is not None:
            return str(self.val) + '->' + self.next.print_forward()
        else:
            return str(self.val)


def unique_pairs(m: int, n: int) -> Tuple[int, int]:
    """Produce pairs of indexes in range(m), range(n)"""
    for i in range(m):
        for j in range(n):
            yield i, j


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


if __name__ == "__main__":
    print(" ".join(islice('ABCDEFG', 2)))
    print(" ".join(islice('ABCDEFG', 2, 2)))
    print(" ".join(islice('ABCDEFG', 2, None)))
    print(" ".join(islice('ABCDEFG', 0, None, 2)))
