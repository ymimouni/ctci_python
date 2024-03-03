from random import choices
from typing import List


def quick_sort(arr: List[int]) -> None:  # noqa
    return r_quick_sort(arr, 0, len(arr) - 1)


def r_quick_sort(arr: List[int], left: int, right: int) -> None:  # noqa
    index = partition(arr, left, right)
    if left < index - 1:
        r_quick_sort(arr, left, index - 1)
    if right > index:
        r_quick_sort(arr, index, right)


def partition(arr: List[int], left: int, right: int) -> int:  # noqa
    pivot = arr[int((left + right) / 2)]  # Pick a pivot.

    while left <= right:
        # Find element on left that should be on right.
        while arr[left] < pivot:
            left += 1

        # Find element on right that should be on left.
        while arr[right] > pivot:
            right -= 1

        # Swap elements and move left and right indices.
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left


if __name__ == "__main__":
    arr = choices(range(0, 100), k=10)
    print(arr)
    quick_sort(arr)
    print(arr)
