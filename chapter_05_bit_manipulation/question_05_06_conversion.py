"""
Conversion.
"""


# def bit_swap_required(a: int, b: int) -> int:
#     t = a ^ b
#     count = 0
#     while t:
#         count += t & 1
#         t = t >> 1
#
#     return count


def bit_swap_required(a: int, b: int) -> int:
    t = a ^ b
    count = 0
    while t:
        count += t & 1
        t = t & (t - 1)

    return count
