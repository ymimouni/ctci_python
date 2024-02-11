"""
Next number.
"""

import unittest


def get_next(n: int) -> int:
    t = n
    c0 = 0
    c1 = 0

    while t & 1 == 0 and t != 0:
        c0 += 1
        t >>= 1

    while t & 1 == 1:
        c1 += 1
        t >>= 1

    # If t is 0, then n is a sequence of 1s followed by a sequence of 0s. This is already the biggest number of c1 ones.
    # Return error.
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    p = c0 + c1  # Position of right most non-trailing zero

    # Flip the right most non-trailing zero
    n |= 1 << p

    # Clear all bits to the right of p
    n &= ~((1 << p) - 1)

    # Put (c1 -1) ones on the right.
    n |= (1 << (c1 - 1)) -1

    return n


def get_prev(n: int) -> int:
    t = n
    c0 = 0
    c1 = 0

    while t & 1 == 1 and t != 0:
        c1 += 1
        t >>= 1

    # If t is 0, then n is a sequence of 0s followed by a sequence of 1s. This is already the smallest number of c1
    # ones. Return error.
    if t == 0:
        return -1

    while t & 1 == 0:
        c0 += 1
        t >>= 1

    p = c0 + c1  # Position of right most non-trailing one

    # Clear from bit p onwards
    n &= ~0 << (p + 1)

    # Creates a sequence of c1 + 1 ones
    mask = (1 << (c1 + 1)) - 1

    # Move the ones to be right up next to p
    n |= mask << (c0 - 1)

    return n


class Test(unittest.TestCase):
    """Test cases."""
    def test_get_next(self):
        self.assertEqual(get_next(10), 12)
        self.assertEqual(get_next(0), -1)
        self.assertEqual(get_next(1879048192), -1)

    def test_get_prev(self):
        self.assertEqual(get_prev(10), 9)
        self.assertEqual(get_prev(0), -1)
        self.assertEqual(get_prev(3), -1)


if __name__ == "__main__":
    unittest.main()
