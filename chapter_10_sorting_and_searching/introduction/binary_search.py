from random import sample
from typing import Optional, List


# def binary_search(arr: List[int], x: int) -> Optional[int]:  # noqa
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         middle = int((left + right) / 2)
#
#         if x == arr[middle]:
#             return middle
#         elif x < arr[middle]:
#             right = middle - 1
#         else:
#             left = middle + 1
#
#     return None


# def binary_search(arr: List[int], x: int) -> Optional[int]:  # noqa
#     return r_binary_search(arr, x, 0, len(arr) - 1)
#
# def r_binary_search(arr: List[int], x: int, left, right) -> Optional[int]:  # noqa
#     if left > right:
#         return None
#
#     middle = int((left + right) / 2)
#
#     if x == arr[middle]:
#         return middle
#     elif x < arr[middle]:
#         return r_binary_search(arr, x, left, middle - 1)
#     else:
#         return r_binary_search(arr, x, middle + 1, right)


def binary_search_closest(arr: List[int], x: int) -> Optional[int]:  # noqa
    return r_binary_search_closest(arr, x, 0, len(arr) - 1)

def r_binary_search_closest(arr: List[int], x: int, left, right) -> Optional[int]:  # noqa
    if right < left:
        if right < 0:
            return left
        if left >= len(arr):
            return right
        if x - arr[right] > arr[left] - x:
            return left
        return right

    middle = int((left + right) / 2)

    if x < arr[middle]:
        return r_binary_search_closest(arr, x, left, middle - 1)
    elif x > arr[middle]:
        return r_binary_search_closest(arr, x, middle + 1, right)
    else:
        return middle


if __name__ == "__main__":
    arr = sorted(sample(range(0, 20), k=10))
    print(arr)
    for e in range(0, 20):
        index = binary_search_closest(arr, e)
        print(f'{e}: {index}')
