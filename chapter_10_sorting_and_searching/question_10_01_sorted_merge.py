from typing import List


def sorted_merge(a: List[int], b: List[int], count_a: int, count_b: int) -> None:
    index_merged = count_a + count_b - 1
    index_a = count_a - 1
    index_b = count_b - 1

    # Merge a and b starting from the last element in each
    while index_b >= 0:
        if index_a >= 0 and b[index_b] < a[index_a]:
            a[index_merged] = a[index_a]
            index_a -= 1
        else:
            a[index_merged] = b[index_b]
            index_b -= 1
        index_merged -= 1
