from random import choices
from typing import List, Optional


def merge_sort(arr: List[int]) -> None:  # noqa
    helper = [None] * len(arr)
    r_merge_sort(arr, helper, 0, len(arr) - 1)


def r_merge_sort(arr: List[int], helper: List[Optional[int]], low: int, high: int) -> None:  # noqa
    if low < high:
        middle = int((low + high) / 2)
        r_merge_sort(arr, helper, low, middle)  # Sort left half
        r_merge_sort(arr, helper, middle + 1, high)  # Sort right half
        merge(arr, helper, low, middle, high)  # Merge them


def merge(arr: List[int], helper: List[Optional[int]], low: int, middle: int, high: int) -> None:  # noqa
    # Copy the elements from the target arr to the helper arr
    helper[low: high + 1] = arr[low: high + 1]

    helper_left = low
    helper_right = middle + 1
    current = low

    # Iterate throw the two halves comparing each time left and right, copying back the smaller element of the two
    # halves into the original array
    while helper_left <= middle and helper_right <= high:
        if helper[helper_left] <= helper[helper_right]:
            arr[current] = helper[helper_left]
            helper_left += 1
        else:
            arr[current] = helper[helper_right]
            helper_right += 1
        current += 1

    # Copy the remaining elements in the left half into the target array. No need to copy the remaining elements of the
    # right half as they are already in the target arr.
    remaining = middle - helper_left
    arr[current: current + remaining] = helper[helper_left: middle]


if __name__ == "__main__":
    arr = choices(range(0, 100), k=20)
    print(arr)
    merge_sort(arr)
    print(arr)
