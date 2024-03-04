from typing import List, Optional


def search(arr: List[int], x: int) -> Optional[int]:  # noqa
    return r_search(arr, x, 0, len(arr) - 1)


def r_search(arr: List[int], x: int, left: int, right: int) -> Optional[int]:  # noqa
    if right < left:  # Not found.
        return None

    middle = int((left + right) / 2)

    if x == arr[middle]:  # Found.
        return middle

    if arr[left] < arr[middle]:  # Left is ordered.
        if arr[left] <= x < arr[middle]:
            return r_search(arr, x, left, middle - 1)
        else:
            return r_search(arr, x, middle + 1, right)
    elif arr[middle] < arr[right]:  # Right is ordred.
        if arr[middle] < middle <= arr[right]:
            return r_search(arr, x, middle + 1, right)
        else:
            return r_search(arr, x, left, middle - 1)
    else:
        location = None
        if arr[left] == arr[middle]:
            location = r_search(arr, x, middle + 1, right)
        if not location and arr[middle] == arr[right]:
            location = r_search(arr, x, left, middle - 1)
        return location


if __name__ == "__main__":
    arr = [15, 16, 19, 19, 21, 1, 3, 5, 7, 7]
    print(f'2: {search(arr, 2)}')
    print(f'2: {search(arr, 1)}')
    print(f'2: {search(arr, 16)}')
    print(f'2: {search(arr, 18)}')
