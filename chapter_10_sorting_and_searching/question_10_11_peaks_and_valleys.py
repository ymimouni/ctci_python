from typing import List


def sort_peak_valley(arr: List[int]) -> None:  # noqa
    for i in range(1, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]


def sort_peak_valley(arr: List[int]) -> None:  # noqa
    for i in range(1, len(arr), 2):
        biggest_index = max_index(arr, i - 1, i, i + 1)
        if i != biggest_index:
            arr[i], arr[biggest_index] = arr[biggest_index], arr[i]


def max_index(arr, i, j, k):  # noqa
    arr_len = len(arr)  # noqa
    i_val = arr[i] if 0 <= i < arr_len else None
    j_val = arr[j] if 0 <= j < arr_len else None
    k_val = arr[k] if 0 <= k < arr_len else None

    max_v = max((x for x in [i_val, j_val, k_val] if x is not None), default=None)  # noqa

    if max_v == i_val:
        return i
    elif max_v == j_val:
        return j
    elif max_v == k_val:
        return k
    else:
        return None


def sort_peak_valley(arr: List[int]) -> None:  # noqa
    for i in range(1, len(arr), 2):
        if arr[i - 1] < arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
        if i + 1 < len(arr) and arr[i + 1] < arr[i]:
            arr[i + 1], arr[i] = arr[i], arr[i + 1]


if __name__ == "__main__":
    arr = [48, 40, 31, 62, 28, 21, 64, 40, 23, 17]
    # arr = sorted(arr)
    print(arr)
    sort_peak_valley(arr)
    print(arr)
