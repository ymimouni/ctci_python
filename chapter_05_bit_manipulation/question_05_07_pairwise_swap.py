"""
Pairwise swap.
"""


def logical_right_shift(n: int) -> int:
    # Assumes that n can be written in 64 bits.
    return (n % 0x100000000) >> 1


def swap_even_odd_bits(n: int) -> int:
    return (logical_right_shift(n & 0xAAAAAAAA)) | ((n & 0x55555555) << 1)
