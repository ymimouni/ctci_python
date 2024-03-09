from random import choices
from typing import List


class BitSet:
    def __init__(self, size):
        self.bit_vector = bytearray(int(size / 8))

    def get(self, pos) -> bool:
        return self.bit_vector[int(pos / 8)] & 1 << (pos % 8)

    def set(self, pos) -> bool:
        self.bit_vector[int(pos / 8)] |= 1 << (pos % 8)


def check_duplicates(arr: List[int]) -> None:  # noqa
    bit_set = BitSet(32000)
    for i, num in enumerate(arr):
        num_0 = num - 1  # bit_set starts at 0, numbers start at 1.
        if bit_set.get(num_0):
            print(num)
        else:
            bit_set.set(num_0)


if __name__ == "__main__":
    arr = choices(range(1, 31), k=30)
    check_duplicates(arr)
