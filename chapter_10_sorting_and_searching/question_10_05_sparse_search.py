from typing import List, Optional


def search(arr: List[str], s: str) -> Optional[int]:  # noqa
    if not s:
        return None

    return r_search(arr, s, 0, len(arr) - 1)


# def r_search(arr: List[str], s: str, left: int, right: int) -> Optional[int]:  # noqa
#     if left > right:
#         return None
#
#     middle = int((left + right) / 2)
#
#     if s == arr[middle]:
#         return middle
#     elif arr[middle]:
#         if arr[middle] > s:
#             return r_search(arr, s, left, middle - 1)
#         elif arr[middle] < s:
#             return r_search(arr, s, middle + 1, right)
#     else:
#         visit_right = True
#         i: int
#         for i in range(middle - 1, left - 1, -1):
#             if arr[i]:
#                 visit_right = False
#                 if arr[i] == s:
#                     return i
#                 elif arr[i] > s:
#                     return r_search(arr, s, left, i - 1)
#                 elif arr[i] < s:
#                     return r_search(arr, s, middle + 1, right)
#         if visit_right:
#             for i in range(middle + 1, right + 1):
#                 if arr[i]:
#                     if arr[i] == s:
#                         return i
#                     elif arr[i] < s:
#                         return r_search(arr, s, i + 1, right)


def r_search(arr: List[str], s: str, first: int, last: int) -> Optional[int]:  # noqa
    while first <= last:

        middle = int((first + last) / 2)

        # If middle is empty, find closest non-empty string.
        if not arr[middle]:
            left = middle - 1
            right = middle + 1
            while True:
                if left < first and right > last:
                    return None
                elif right <= last and arr[right]:
                    middle = right
                    break
                elif left >= first and arr[left]:
                    middle = left
                    break
                left -= 1
                right += 1

        if arr[middle] == s:
            return middle
        elif arr[middle] > s:
            last = middle - 1
        else:
            first = middle + 1

    return None


if __name__ == "__main__":
    arr = ['apple', '', '', 'banana', '', '', '', 'carrot', 'duck', '', '', 'eel', '', 'flower']
    s = 'ac'
    print(f'{s}: {search(arr, s)}')
