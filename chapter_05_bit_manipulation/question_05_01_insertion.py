""""
Insertion.
"""


# Returns bit x of y (10 base). i.e.
# bit 2 of 5 is 1
# bit 1 of 5 is 0
# bit 0 of 5 is 1
def get_bit(y, x):
    return str((y >> x) & 1)


# Returns the first count bits of base 10 integer y
def to_bin(y, count=32):
    shift = range(count - 1, -1, -1)
    bits = map(lambda x: get_bit(y, x), shift)
    return "".join(bits)


def insert(n: int, m: int, i: int, j: int) -> int:
    if i > j or i < 0:
        return 0

    # Create a mask to clear bits i to j in n.
    left = ~0 << (j + 1)  # 1s before position j.
    right = (1 << i) - 1  # 1s after postion i.

    # All 1s, except for 0s between i and j.
    mask = left | right

    # Clear bits j through i then put m in there.
    n_cleared = n & mask
    m_shifted = m << i

    return n_cleared | m_shifted


if __name__ == "__main__":
    print(insert(~23423, 5, 29, 31))
