from typing import List, Optional, Tuple, Dict


# def make_change(n: int, denoms: List[int], index: int) -> int:  # noqa
#     return r_make_change(n, denoms, 0)
#
#
# def r_make_change(total: int, denoms: List[int], index: int):  # noqa
#     coin = denoms[index]
#     if index == len(denoms) - 1:
#         remaining = total % coin
#         return 1 if not remaining else 0
#
#     ways = 0  # noqa
#
#     for amount in range(0, total + 1, coin):
#         ways += r_make_change(total - amount, denoms, index + 1)
#
#     return ways


# def make_change(n: int, denoms: List[int], index: int) -> int:  # noqa
#     change_map = [[None] * len(denoms) for _ in range(n + 1)]
#     return r_make_change(n, denoms, 0, change_map)
#
#
# def r_make_change(total: int, denoms: List[int], index: int, change_map: List[List[Optional[int]]]):  # noqa
#     if change_map[total][index]:
#         return change_map[total][index]
#
#     coin = denoms[index]
#     if index == len(denoms) - 1:
#         remaining = total % coin
#         return 1 if not remaining else 0
#
#     ways = 0  # noqa
#
#     for amount in range(0, total + 1, coin):
#         ways += r_make_change(total - amount, denoms, index + 1, change_map)
#
#     change_map[total][index] = ways
#
#     return ways


# def make_change(n: int, denoms: List[int], index: int) -> int:  # noqa
#     change_map = {}
#     return r_make_change(n, denoms, 0, change_map)
#
#
# def r_make_change(total: int, denoms: List[int], index: int, change_map: Dict[Tuple[int, int], int]):  # noqa
#     if (total, index) in change_map:
#         return change_map[(total, index)]
#
#     coin = denoms[index]
#     if index == len(denoms) - 1:
#         remaining = total % coin
#         return 1 if not remaining else 0
#
#     ways = 0  # noqa
#
#     for amount in range(0, total + 1, coin):
#         ways += r_make_change(total - amount, denoms, index + 1, change_map)
#
#     change_map[(total, index)] = ways
#
#     return ways


# def make_change(n: int, denoms: List[int], index: int) -> int:  # noqa
#     change_map = {}
#     return r_make_change(n, denoms, 0, change_map)
#
#
# def r_make_change(total: int, denoms: List[int], index: int, change_map: Dict[int, Dict[int, int]]):  # noqa
#     if total in change_map and index in change_map[total]:
#         return change_map[total][index]
#
#     coin = denoms[index]
#     if index == len(denoms) - 1:
#         remaining = total % coin
#         return 1 if not remaining else 0
#
#     ways = 0  # noqa
#
#     for amount in range(0, total + 1, coin):
#         ways += r_make_change(total - amount, denoms, index + 1, change_map)
#
#     if total in change_map:
#         change_map[total][index] = ways
#     else:
#         index_d = {index: ways}
#         change_map[total] = index_d
#
#     return ways


def make_change(n: int, denoms: List[int], index: int) -> int:  # noqa
    change_map = {}
    return r_make_change(n, denoms, 0, change_map)


def r_make_change(total: int, denoms: List[int], index: int, change_map: Dict[int, Dict[int, int]]):  # noqa
    if total in change_map:
        temp_map = change_map[total]
        if index in temp_map:
            return temp_map[index]

    coin = denoms[index]
    if index == len(denoms) - 1:
        remaining = total % coin
        return 1 if not remaining else 0

    ways = 0  # noqa

    for amount in range(0, total + 1, coin):
        ways += r_make_change(total - amount, denoms, index + 1, change_map)

    if total in change_map:
        change_map[total][index] = ways
    else:
        index_d = {index: ways}
        change_map[total] = index_d

    return ways


def test_make_change():
    n = 3541
    denoms = [25, 10, 5, 1]
    make_change(n, denoms, 0)
    # print(make_change(n, denoms, 0))


if __name__ == "__main__":
    import timeit
    print(timeit.timeit("test_make_change()", setup="from __main__ import test_make_change", number=100))
    # test_make_change()
